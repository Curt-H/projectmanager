from flasky.app import create_app

if __name__ == '__main__':
    app = create_app()
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=80,
    )
    app.run(**config)
