-----------------------------------------------------------------------------
                    ::: HTML :::
-----------------------------------------------------------------------------


-----------------------------------------------------------------------------
                    ::: CSS :::
-----------------------------------------------------------------------------



-----------------------------------------------------------------------------
                     :::: RESPONSIVE ::::
-----------------------------------------------------------------------------


There are four (4) different ways to make web page as Responsive.
    i. Viewport:-
        eg: <meta name="viewport" content="width=device-width, initial-scale=1.0">

   ii. Media Queries:-
        eg: <style>
                @media (min-width = 600px) {
                    background-color: red;
                    font-family: bold;
                    font-size: 50px;
                }
                @media (max-width=500px) {
                    background-color: blue;
                }

  iii. Flex box:-
    eg: <style>
        #container {
            display: flex;
            flex-wrap: wrap;
        }
        #container > div {
            background-color: green;
            font-size: 10px;
            font-weight: bold;
        }
      </style>

      
   iv. Grids:-

   <style>
        #grid {
            background-color: green;
            display: grid;
            padding: 20px;
            grid-column-gap: 20px;
            grid-row-gap: 20px;
            grid-template-columns: 200px 200px auto;
        }

        .grid-item {
            background-color: white;
            font-size: 20px;
            padding:20px;
        }
    </style>
    ---------------------------------------------------------------------------

                            :Bootstrap:

        col-12 (complete page)
        col-6 (half page)
        col-4 (quater page)

        col-lg-3 (for large page width = 3)
        col-sm-6 (for small page/device width = 6)
        col-md-10 (for mobile device width = 10)

    
---------------------------------------------------------------------------------

                                : SASS :

1. styles.scss

    $color: blue;

    .header {
        color: $color;
    }
    ul {
        color: $color;
    }

2. styles.scss

    %message {
        font-size:20px;
        font-weight: bold;
        margin: 20px;
        padding: 20px;
    }

    .success {
        @extend %message;
        background-color: green;
    }

    .warning {
        @extend %message;
        background-color: orange;
    }

    .danger {
        @extend %message;
        background-color: red;
    }

Note: To run scss files into html file, we have to convert to css.
    -> sass styles.scss:styles.css (converts from scss -> css)
                or
    -> sass --watch styles.scss:styles.css 

-----------------------------------------------------------------------------------
                        :::: GIT ::::
-----------------------------------------------------------------------------------
