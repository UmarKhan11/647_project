<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CART</title>
    <link rel="stylesheet" href="styles/css/style.css">
    <link rel="stylesheet" href="styles/css/cart.css">
    <link rel="stylesheet" href="styles/bs_css/css/bootstrap.css">
  </head>
  <body>

     <!-- ?php -->
        <!-- $mysqli = new mysqli("mysql.eecs.ku.edu", "U250K480", "EeV9sae4", "U250K480") or die("Cannot connect to server");
        $resultSet = $mysqli->query("SELECT CRUISE.* FROM CRUISE");
        while ($rows = $resultSet->fetch_assoc()) {
            $name = $rows['DIRECTOR'];
            echo "<h1>$ $name </h1>";
        } -->
    <!-- ?>  -->

      
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
            <a class="nav-link active" aria-current="page" href="#">HOME</a>
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
                <li><a class="dropdown-item" href="#">LOGIN</a></li>
                <li><hr class="dropdown-divider"></li>
                <li><a class="dropdown-item" href="#">WISHLIST</a></li>
                <li><a class="dropdown-item" href="#">CART</a></li>
            </ul>
            </li>
        </ul>
        </div>
    </div>
  </nav>

    <!-- CART STUFF -->
    <div class="store-layout">
        <div class="cart-wrapper">
            <h1>MY CARTS</h1>
            <div class="cart-item-wrapper ">
                <div id="cart-items">
                <div class="cart-card cart-card-header ">
                    <div class="card-format">
                        CART_ID
                    </div>
                    <div class="card-format">
                        USERNAME
                    </div>
                    <button class="card-format btn btn-primary">
                        VIEW CART
                    </button>
                </div>
                </div>
            </div>
        </div>
            <div class="current-cart-wrapper">
                <h1>CURRENT CART:</h1>
                <div class="table-format">
                    <table class="table">
                    <tr>
                        <th>USERNAME</th>
                        <th>CART_ID</th>
                        <th>PRODUCT_ID</th>
                        <th>PRODUCT_NAME</th>
                        <th>PRICE</th>
                        <th>QUANTITY</th>

                    </tr>
                    <tr>
                        <td>UMI</td>
                        <td>0</td>
                        <td>0</td>
                        <td>ADIDAS NMD SHOES MENS</td>
                        <td>140</td>
                        <td>1</td>
                    </tr>
                    </table>
                </div>
            </div>
        </div>
    </div>

    <script src="styles/js/index.js"></script>
    <script src="styles/js/cart.js"></script>
	<script src="styles/bs_js/js/bootstrap.js"></script>
  </body>
</html>