def create_HTML(df: pd.DataFrame) -> None: #creates html table and opens it in browser
    css_style = """
    <style>

    body {
        background-color: white;
        border: 4px solid #ddd;
    }
    table, th, td, tr {
        border: 1px solid black; 
        color: black;
        border-collapse: collapse;
        min-width:100px;
    }
    tr:nth-child(even) {
        background-color: rgba(150, 212, 212, 0.4);
    }
    
    td:nth-child(even) {
        background-color: rgba(150, 212, 212, 0.4);
    }

    th{
        text-align: left;
        top: 0;
        position: sticky;
        background-color: rgba(150, 212, 212, 0.99);
    }
    
    tr:hover {background-color: #ffff61;}
    </style>
    """

    result = df.to_html()

    try:
        text_file = open("Instructions.html", "w")
    except:
        text_file = open("Instructions.html", "x")
    text_file.write(css_style+result)
    text_file.close()
    webbrowser.open_new_tab("Instructions.html")
    return
