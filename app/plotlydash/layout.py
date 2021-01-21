"""Plotly Dash HTML layout override."""

html_layout = """
<!doctype html>
<html lang="en" class="h-100">
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" integrity="sha384-wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN" crossorigin="anonymous">
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
    <!-- Google Fonts -->
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"/>
    <!-- Custom CSS for Dash -->
    <link rel="stylesheet" href="/static/dashstyles.css">
    <!-- Custom CSS -->
    <link rel="stylesheet" href="/static/style.css">

    <!-- bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" async integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>
    <title>Data + Visualizations</title>
</head>
<body class="d-flex flex-column h-100 body">
<nav class="navbar navbar-expand-lg navbar-light bg-white shadow">
    <div class="container">
        <a class="navbar-brand" href="#"><span class="fa fa-medkit"></span> ML Diabetes Diagnosis</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <li class="nav-item">
                    <a class="nav-link " href="/">Home</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link " href="/diagnose">Diagnosis</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link active" href="#">Data + Visualizations</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link " href="/about">About</a>
                </li>
            </ul>
        </div>
    </div>
</nav>
<main role="main" class="flex-shrink-0">
    <div class="container shadow rounded fadeIn p-5 my-5 bg-white" id="content">

    <h2> Data Visualization </h2>
    <br>
            {%app_entry%}
    </div>
</main>
<footer class="footer mt-auto py-3 text-white">
    <div class="container">
        <div class="d-flex justify-content-between">
            <div>
                <span class="text-white small">Dylan Cairns 2020</span>
            </div>
            <div class>
                <a class="text-white text-decoration-none" href="https://github.com/">View the source on Github <i class="fa fa-github"></i></a>
            </div>
        </div>
    </div>
                {%config%}
                {%scripts%}
                {%renderer%}
</footer>
</body>
</html>
"""