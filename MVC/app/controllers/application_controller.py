from MVC.app.models.user import *
from MVC.app.views.new import *
from MVC.app.views.show import *
from MVC.app.views.edit import *
from MVC.app.views.destroy import *
import os


class application_controller:
    def new():
        # method new() dans views new
        result = new()
        save(result[0], result[1])

    def all_():
        # method show_all dans views show
        all_ = show_all()
        show(all_)

    def update():
        # method show_all dans model user
        all_ = show_all()
        # method dans views edit
        r = edit(all_)
        update(r[0], r[1], r[2])

    def delete():
        # method show_all dans model user
        all_ = show_all()
        r = destroy(all_)
        delete(r)


os.system("black app/controllers/application_controller.py")
