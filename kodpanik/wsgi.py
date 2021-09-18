from kodpanik.core import create_app

if __name__ == '__main__':
    app = create_app(config="kodpanik.core.config.settings")
    app.run()
