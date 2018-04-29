name := "AllNews"

version := "0.1"

scalaVersion := "2.10.6"

val sparkVersion = "2.0.0"

libraryDependencies ++= Seq(
  "org.apache.spark" %% "spark-core" % sparkVersion,
  "org.apache.spark" %% "spark-sql" % sparkVersion,
  "org.apache.spark" %% "spark-mllib" % sparkVersion,
  "edu.stanford.nlp" % "stanford-corenlp" % "3.6.0",
  "com.google.protobuf" % "protobuf-java" % "2.6.1",
  "edu.stanford.nlp" % "stanford-corenlp" % "3.6.0" % "test" classifier "models",
  "org.scalatest" %% "scalatest" % "2.2.6" % "test"
)
libraryDependencies += "databricks" % "spark-corenlp" % "0.2.0-s_2.11"