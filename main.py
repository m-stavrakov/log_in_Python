from website import create_app

app = create_app()

if __name__ == '__main__': #this means only if we run this file the line below will be executed
    app.run(debug=True) 