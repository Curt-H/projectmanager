from flasky.app import create_app

if __name__ == '__main__':
    app = create_app()
    config = dict(
        debug=True,
        host='localhost',
        port=80,
    )
    app.run(**config)
