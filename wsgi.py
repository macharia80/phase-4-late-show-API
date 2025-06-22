from server import create_app

app = create_app()  # This should match your create_app function name

if __name__ == "__main__":
    app.run(debug=True)