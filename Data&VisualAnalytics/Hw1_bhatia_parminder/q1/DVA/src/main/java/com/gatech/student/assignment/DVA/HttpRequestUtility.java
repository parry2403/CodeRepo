package com.gatech.student.assignment.DVA;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.URL;
import java.net.URLConnection;
import java.net.URLEncoder;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;

import org.json.JSONArray;
import org.json.JSONObject;

public class HttpRequestUtility {

	/**
	 * Makes a HTTP request to a URL and receive response
	 * 
	 * @param requestUrl
	 *            the URL address
	 * @param method
	 *            Indicates the request method, "POST" or "GET"
	 * @param params
	 *            a map of parameters send along with the request
	 * @return An array of String containing text lines in response
	 * @throws IOException
	 */
	public static ArrayList<MyTrack> sendHttpRequest(String requestUrl,
			String method, Map<String, String> params) throws IOException {
		List<String> response = new ArrayList<String>();

		StringBuffer requestParams = new StringBuffer();
		ArrayList<MyTrack> similarTracks = new ArrayList<MyTrack>();

		if (params != null && params.size() > 0) {
			Iterator<String> paramIterator = params.keySet().iterator();
			while (paramIterator.hasNext()) {
				String key = paramIterator.next();
				String value = params.get(key);
				requestParams.append(URLEncoder.encode(key, "UTF-8"));
				requestParams.append("=").append(
						URLEncoder.encode(value, "UTF-8"));
				requestParams.append("&");
			}
		}

		URL url = new URL(requestUrl);
		URLConnection urlConn = url.openConnection();
		urlConn.setUseCaches(false);

		// the request will return a response
		urlConn.setDoInput(true);

		if ("POST".equals(method)) {
			// set request method to POST
			urlConn.setDoOutput(true);
		} else {
			// set request method to GET
			urlConn.setDoOutput(false);
		}

		if ("POST".equals(method) && params != null && params.size() > 0) {
			OutputStreamWriter writer = new OutputStreamWriter(
					urlConn.getOutputStream());
			writer.write(requestParams.toString());
			writer.flush();
		}

		// reads response, store line by line in an array of Strings
		BufferedReader reader = new BufferedReader(new InputStreamReader(
				urlConn.getInputStream()));

		String line = "";
		while ((line = reader.readLine()) != null) {
			System.out.println(line);
			response.add(line);
			JSONObject jObject = new JSONObject(line); // json
		    JSONObject data = jObject.getJSONObject("similartracks"); // get
																		// data
																		// object
			JSONArray tracks = (JSONArray) data.get("track");

			System.out.println(tracks.get(0));
			System.out.println(tracks.length());
			for (int i = 0; i < tracks.length(); i++) {
				MyTrack mytrack = new MyTrack();
				mytrack.setArtist(((JSONObject) tracks.get(i)).getJSONObject(
						"artist").getString("name"));
				mytrack.setMbid(((JSONObject) tracks.get(i)).getString("mbid"));
				mytrack.setName(((JSONObject) tracks.get(i)).getString("name"));
				similarTracks.add(mytrack);
			}
		}

		reader.close();

		return similarTracks;
	}

	public static void main(String args[]) {
		String requestUrl = "http://ws.audioscrobbler.com/2.0/?method=track.getsimilar&artist=Madonna&track=Hung Up&api_key=48ebaacdbca6c6c432737276bb35f09c&format=json&limit=5";
		String method = "GET";
		Map<String, String> params = new HashMap<String, String>();
		String url ="http://ws.audioscrobbler.com/2.0/?method=track.getsimilar&artist=Madonna&track=Hung Up&limit=5&api_key=48ebaacdbca6c6c432737276bb35f09c&format=json";
		System.out.println("started");
		try {
			ArrayList<MyTrack> response = HttpRequestUtility.sendHttpRequest(
					requestUrl, method, params);
			for (MyTrack current : response) {
				System.out.println(current.getName() + " *********** "
						+ current.getMbid());

			}

		} catch (IOException ex) {
			System.out.println("ERROR: " + ex.getMessage());
		}
	}

}