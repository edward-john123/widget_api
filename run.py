from app import create_app

# run with gunicorn
app = create_app()

# for dev server
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
