<?php include 'masterpages/header.php'; 
	include 'classes/prodInfoEnum.php';
	# Get product after escaping input
	$product; $infoNames; $productInfo;
	if(ISSET($_REQUEST['pid'])) {
		$prodId = htmlspecialchars($_REQUEST['pid'], ENT_QUOTES);
		$product = $DBHelper->GetProductById($prodId);
		$infoNames = $DBHelper->GetInfoNamesByProductId($prodId);
		$productInfo = $DBHelper->GetProductInfoValuesByProductId($prodId);
	}
	else {
		echo "Some error";
	}
	echo sprintf('<h2>%s</h2>', $product->name);
	echo sprintf('<p class="productInfo textLeft">%s</p>', $product->desc);
	echo sprintf('<div class="productImgContainer"><img src="images/products/%s" /></div>', $product->img);	

	echo '<table class="productSpecs">
			<thead>
				<tr>';
	foreach($infoNames as $iv) {
		echo sprintf('<th>%s</th>', ProdInfoEnum::RealName($iv->id));
	}
	echo '</tr></thead><tbody><tr>';
	$collectionNo = 1;
	$nextAlt = true;
	foreach($productInfo as $pi) {
		foreach($pi as $innerPi) {
			if($innerPi->collectionNo != $collectionNo) # New row
			{
				if(!$nextAlt) {
					echo '</tr><tr>';
					$nextAlt = true;
				}
				else {
					echo '</tr><tr class="alternate">';
					$nextAlt = false;
				}
				$collectionNo = $innerPi->collectionNo;
			}
			
			# "Lagervara" should be green
			if($innerPi->value !== "Lagervara") {
				echo sprintf('<td>%s</td>', $innerPi->value);
			}
			else {
				echo sprintf('<td class="green">%s</td>', $innerPi->value);
			}
		}
	}
	echo '</tbody></table>';
?>

<?php include 'masterpages/footer.html' ?>
