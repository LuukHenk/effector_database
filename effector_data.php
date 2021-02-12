<?php
$conn = new mysqli('localhost', 'root', '', 'effector_data');
if($conn->connect_error){
	die('Connection Failed:'.$conn->connect_error);
} else {

	if (isset($_POST['submit'])) {
		$effector_id_post = $_POST['effector_id--post'];
		$effector_dna_seq = $_POST['effector_dna_seq'];
		$stmt = $conn->prepare("INSERT INTO sequence (effector_id, effector_dna_seq) VALUES (?, ?)");
		$stmt->bind_param("ss", $effector_id_post, $effector_dna_seq);
		$stmt->execute();
		echo "Added sequence to the database!";
		$stmt->close();
	} elseif (isset($_POST['fetch'])) {
		$effector_id_fetch = $_POST['effector_id--fetch'];
		$sql = "SELECT effector_id, effector_dna_seq FROM sequence WHERE effector_id LIKE '%$effector_id_fetch%'";
		$result = $conn->query($sql);
		if ($result->num_rows > 0) {
			// output data of each row
			echo $effector_id_fetch."<br>";
			while($row = $result->fetch_assoc()) {
				echo "Effector ID: " . $row["effector_id"]. " - Effector sequence: " . $row["effector_dna_seq"]. "<br>";
			}
		} else
			echo "no data found...";
	}
	$conn->close();
}


?>
