from apps import create_app

settings_module = 'config.desarrollo.Configuracion'
app = create_app(settings_module)

if __name__ == '__main__':
    app.run(port=5000)