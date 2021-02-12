<?php

if (isset($_POST['submit'])) {
	$effector_id = $_POST['effector_id'];
	$effector_dna_seq = $_POST['effector_dna_seq'];

	$conn = new mysqli('localhost', 'root', '', 'effector_data');
	if($conn->connect_error){
		die('Connection Failed:'.$conn->connect_error);
	}else{
		$stmt = $conn->prepare("INSERT INTO sequence (effector_id, effector_dna_seq) VALUES (?, ?)");
		$stmt->bind_param("ss", $effector_id, $effector_dna_seq);
		$stmt->execute();
		echo "Added sequence to the database!";
		$stmt->close();
		$conn->close();
	}
}
?>
