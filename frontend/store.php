<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>STORE</title>
    <link rel="stylesheet" href="styles/css/style.css">
    <link rel="stylesheet" href="styles/css/store.css">
    <link rel="stylesheet" href="styles/bs_css/css/bootstrap.css">
  </head>
  <body>
      
  <!-- NAVBAR -->
  <nav class="navbar navbar-expand-lg navbar navbar-dark bg-dark">
    <div class="container-fluid">
        <a class="navbar-brand" href="#">|  D A - B R O W N S  |</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
            <a class="nav-link" aria-current="page" href="#">HOME</a>
            </li>
            <li class="nav-item">
            <a class="nav-link" href="#">STORE</a>
            </li>
            <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                ACCOUNT
            </a>
            <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                <li><a class="dropdown-item" href="#">MY PROFILE</a></li>
                <li><hr class="dropdown-divider"></li>
                <li><a class="dropdown-item" href="#">WISHLIST</a></li>
                <li><a class="dropdown-item" href="#">CART</a></li>
            </ul>
            </li>
        </ul>
        </div>
    </div>
  </nav>

<!-- STORE STUFF -->
    <div class="store-layout">
        <div class="store-filter">
            <div class="store-filter-option">
                <a href="#">BRAND</a>
                <div class="store-filter-sub-options">
                    <a href="#">NIKE</a>
                </div>
                <div class="store-filter-sub-options">
                    <a href="#">ADIDAS</a>
                </div>
            </div>
            <div class="store-filter-option">
                <a href="#">CATEGORY</a>
                <div class="store-filter-sub-options">
                    <a href="#">CLOTHES</a>
                </div>
                <div class="store-filter-sub-options">
                    <a href="#">SHOES</a>
                </div>
            </div>
            <div class="store-filter-option">
                <a href="#">PRICE RANGE</a>
                <div class="store-filter-sub-options">
                    <a href="#">$0 - $25</a>
                </div>
                <div class="store-filter-sub-options">
                    <a href="#">$25 - $50</a>
                </div>
                <div class="store-filter-sub-options">
                    <a href="#">$50 - $75</a>
                </div>
                <div class="store-filter-sub-options">
                    <a href="#">$75 - +$100</a>
                    </div>
            </div>
            <div class="store-filter-option">
                <a href="#">$ - $$$</a>
            </div>
            <div class="store-filter-option">
                <a href="#">$$$ - $</a>
            </div>
        </div>
        <div class="store-items" id="store-items">

        </div>
    </div>

	<script src="styles/js/index.js"></script>
	<script src="styles/js/store.js"></script>
	<script src="styles/bs_js/js/bootstrap.js"></script>
  </body>
</html>