from website import create_app  # import this def from the __init_ file in folder 'website' (which acts as a package as a result of containing the __init__ file)

app = create_app()

if __name__ == '__main__':    # only if we run this specific file will the following run (and not when imported)
    app.run(debug=True, host='0.0.0.0')       # debug=True means any changes to the code reruns the web server