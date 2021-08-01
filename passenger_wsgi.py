import heckguide.wsgi
from whitenoise import WhiteNoise

application = heckguide.wsgi.application
application = WhiteNoise(application, root='/home/heckkciy/dev.heckguide.com/static')