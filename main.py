from website import create_app
import random

app = create_app()

if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0', port=random.randint(2000, 9000))
  #app.run(debug=True)
