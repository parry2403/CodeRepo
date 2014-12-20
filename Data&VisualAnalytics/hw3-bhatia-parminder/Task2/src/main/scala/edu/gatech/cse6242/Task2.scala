package edu.gatech.cse6242

import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._
import org.apache.spark.SparkConf

object Task2 {
  def main(args: Array[String]) {
    val sc = new SparkContext(new SparkConf().setAppName("Task2"))

    // read the file
    val file = sc.textFile("hdfs://localhost:8020" + args(0))
 //	val line = file.flatMap(_.split("\n"))
 
    // count the occurrence of each word
    val wordCounts = file.map(s =>  (s.split("\t")(1),s.split("\t")(2).toInt)  ).reduceByKey(_ + _)
 
    /* need to be implemented */

    // store output on given HDFS path.
    // YOU NEED TO CHANGE THIS
   
     var outformat = wordCounts.map(s =>s._1 + '\t' + s._2)
     
   outformat.saveAsTextFile("hdfs://localhost:8020" + args(1))
  }
}
