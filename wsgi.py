from app import create_app

__author__ = 'Joe Robertson'
__credits__ = ['Joe Robertson']

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0')