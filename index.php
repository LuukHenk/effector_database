<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8">
		<!-- Make sure the website works on all screen sizes -->
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>Effector_database</title>
		<!-- Normalization between browsers -->
		<link rel="stylesheet"
			href="https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.1/normalize.css">
		<link>
		<link rel="stylesheet" href="css/style.css">
	</head>

	<body>
		<div class="main_container">
			<div class="input_container">
				<form action="effector_data.php" method="post">
					<div class="form_group">
						<label for="effector_id">Effector ID</label>
						<input class="form_control" type="text" name="effector_id" placeholder="e.g. fasta_123"/>
					</div>

					<div class="form_group">
						<label for="effector_dna_seq">Effector DNA sequence</label>
						<input class="form_control" type="text" name="effector_dna_seq" placeholder="ACTG"/>
					</div>
					<button type="submit" name="submit">Send</button>
				</form>

			</div>
		</div>
	</body>

</html>

