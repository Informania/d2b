<?php include('masterpages/header.php'); 
	if(ISSET($_REQUEST['category'])) {
		$category = htmlspecialchars($_REQUEST['category'], ENT_QUOTES);
		$oneCategory = true;
	}
	else {
		$oneCategory = false;
		$category = '';	
	}

	if($oneCategory) {	
		$productGroups = $DBHelper->GetProductGroupsByCategory($category);

		echo '<div class="row textCenter">';

		echo sprintf("<h2>%s</h2>", $category);
		foreach($productGroups as $pg) {
			$onClickStr = sprintf('location.href=\'distanser.php?group=%s\'', $pg->name);
			echo sprintf('
				<div onclick="%3$s" class="card">
					<img src="images/products/%2$s" />
					<p class="cardCaption">%1$s</p>
				</div>', $pg->name, $pg->img, $onClickStr);
		}
		echo '</div>';
	}
	else {
		$categories = $DBHelper->GetProductCategories();
		foreach($categories as $cat) {
			echo '<div class="row textCenter">';	
			echo sprintf("<h2>%s</h2>", $cat->name);
			//TODO: Maybe get all productgroups and select the ones
			//with the current categoryId?
			$productGroups = $DBHelper->GetProductGroupsByCategory($cat->name);
			foreach($productGroups as $pg) {
				$onClickStr = sprintf('location.href=\'distanser.php?group=%s\'', $pg->name);
				echo sprintf('
					<div onclick="%3$s" class="card">
						<img src="images/products/%2$s" />
						<p class="cardCaption">%1$s</p>
					</div>', $pg->name, $pg->img, $onClickStr);
			}
			echo '</div>';


		}

	}
?>
<?php include('masterpages/footer.html'); ?>
