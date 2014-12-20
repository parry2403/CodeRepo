package com.gatech.student.assignment.DVA;

import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;

import de.umass.lastfm.Track;

public class DataCollection {

	private static String key = "48ebaacdbca6c6c432737276bb35f09c";
	private static String artist = "cher";
	private static String track = "believe";

	public ArrayList<MyTrack> getSimilarTracks(String artist, String track,
			String key, int count) {
		int current = 0;
		Collection<Track> tracks = Track.getSimilar(artist, track, key);
		Iterator<Track> itr = tracks.iterator();
		ArrayList<MyTrack> similarTracks = new ArrayList<MyTrack>();

		while (itr.hasNext()) {
			if (current >= count) {
				break;
			}
			Track currentTrack = itr.next();
			if (null != currentTrack.getMbid()
					&& !currentTrack.getMbid().isEmpty()) {
				// Supermodel%20(You%20Better%20Work)

				// System.out.println("");
				if (!(currentTrack.getName().equals("Hung Up")
						|| currentTrack.getName().equals("If You Had My Love") || currentTrack
						.getName().equals("Supermodel (You Better Work)"))) {
					MyTrack mytrack = new MyTrack();
					mytrack.setArtist(currentTrack.getArtist());
					mytrack.setMbid(currentTrack.getMbid());
					mytrack.setName(currentTrack.getName());
					similarTracks.add(mytrack);
					current++;
				}
			}
		}
		return similarTracks;
	}

	public Map<MyTrack, List<MyTrack>> getConnectedSimilarTracks(String artist,
			String track, String key, int count, int connections)
			throws IOException {
		ArrayList<MyTrack> tracks = this.getSimilarTracks(artist, track, key,
				count);
		System.out.println("Similar Tracks ***************");
		for (MyTrack mTrack : tracks) {
			System.out.println(mTrack.getArtist());
			System.out.println(mTrack.getMbid());
		}
		Map<MyTrack, List<MyTrack>> relation = new HashMap<MyTrack, List<MyTrack>>();
		for (MyTrack similarTrack : tracks) {

			String id = replace(similarTrack.getName(), " ", "%20");

			try {
				relation.put(
						similarTrack,
						getSimilarTracks(similarTrack.getArtist(),
								similarTrack.getName(), key, connections));
			} catch (Exception e) {
				// System.out.println("id******   " + id);
				//
				// StringBuilder st = new StringBuilder(
				// "http://ws.audioscrobbler.com/2.0/?method=track.getsimilar&api_key=48ebaacdbca6c6c432737276bb35f09c&format=json");
				// st.append("&artist=" + similarTrack.getArtist());
				// st.append("&track=" + similarTrack.getName());
				// st.append("&limit=" + connections);
				// System.out.println(st.toString());
				// ArrayList<MyTrack> response = HttpRequestUtility
				// .sendHttpRequest(st.toString(), "GET", null);
				// relation.put(similarTrack, response);
			}
		}

		return relation;

	}

	private static void generateTrackCsvFile(String sFileName,
			List<MyTrack> tracks) {
		try {
			FileWriter writer = new FileWriter(sFileName);

			writer.append("id");
			writer.append(',');
			writer.append("track_name");
			writer.append(',');
			writer.append("artist");
			writer.append('\n');

			for (MyTrack track : tracks) {
				writer.append(track.getMbid());
				writer.append(',');
				writer.append(track.getName());
				writer.append(',');
				writer.append(track.getArtist());
				writer.append('\n');
			}

			writer.flush();
			writer.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	private static void generatePairCsvFile(String sFileName,
			Map<MyTrack, List<MyTrack>> connections) {
		Map<String, String> common = new HashMap<String, String>();

		try {
			FileWriter writer = new FileWriter(sFileName);

			writer.append("source");
			writer.append(',');
			writer.append("target");
			writer.append('\n');

			for (MyTrack track : connections.keySet()) {
				if (!(null == track.getMbid() || track.getMbid().isEmpty())) {

					for (MyTrack linked : connections.get(track)) {
						if (!(null == linked.getMbid() || linked.getMbid()
								.isEmpty())) {
							if (common.containsKey(linked.getMbid()
									+ track.getMbid())
									|| common.containsKey(track.getMbid()
											+ linked.getMbid())) {
								// Do nothing
							} else {
								writer.append(track.getMbid());
								writer.append(',');
								writer.append(linked.getMbid());
								writer.append('\n');
								common.put(linked.getMbid() + track.getMbid(),
										linked.getMbid() + track.getMbid());
							}
						}

					}
				}

			}

			writer.flush();
			writer.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	public static void main(String args[]) throws IOException {
		DataCollection dCollection = new DataCollection();

		ArrayList<MyTrack> tracks = dCollection.getSimilarTracks(artist, track,
				key, 100);

		Map<MyTrack, List<MyTrack>> connections = dCollection
				.getConnectedSimilarTracks(artist, track, key, 100, 10);

		// for (MyTrack current : connections.keySet()) {
		// System.out.println(current.getName() + " *********** "
		// + current.getMbid());
		// for (MyTrack similar : connections.get(current)) {
		// System.out.println(similar.getName());
		// }
		// }
		generateTrackCsvFile("c:\\tracks.csv", tracks);
		generatePairCsvFile("c:\\track_id_sim_track_id.csv", connections);

	}

	private final static String replace(String text, String searchString,
			String replacementString) {
		StringBuffer sBuffer = new StringBuffer();
		int pos = 0;

		while ((pos = text.indexOf(searchString)) != -1) {
			sBuffer.append(text.substring(0, pos) + replacementString);
			text = text.substring(pos + searchString.length());
		}

		sBuffer.append(text);
		return sBuffer.toString();
	}
}
