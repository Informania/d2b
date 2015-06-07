<?php include 'masterpages/header.php'; 

	# Get products for given category after escaping input
	$products;
	if(ISSET($_REQUEST['c'])) {
		$group = htmlspecialchars($_REQUEST['c'], ENT_QUOTES);
		$products = $DBHelper->GetProductsByGroup($group);
	}
	else {
		echo "Some error";
	}
	$headerString;
	if($group == "Runda")
		$headerString = "<h2>Runda distanser</h2>";
	else
		$headerString = "<h2>Distanser för %s</h2>";
	echo sprintf($headerString, $group);
	# Display the products
	foreach($products as $product) {
		echo sprintf('<div class="card" onclick="location.href=\'produkt.php?pid=%d\'";>', $product->id);	
		echo sprintf('<img src="images/%s" />', $product->img !== null ? $product->img : "missing.png");
        echo sprintf('<p class="cardCaption">%s</p>', $product->name);
		echo '</div>';
	}	


?>





<?php include 'masterpages/footer.html' ?>
