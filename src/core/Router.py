import inspectclass Router:    def registry(self, app, routes, handlres):        for path, method, handler in routes:            controller = self.matchController(handlres, handler)            if "Controller" not in handler.__qualname__ and isinstance(handler, types.FunctionType):                app.add_url_rule(path, methods=method, view_func=handler)            elif (controller is not None and hasattr(controller, handler.__name__)):                app.add_url_rule(path, methods=method, view_func=getattr(controller, handler.__name__))            else:                raise Exception("Handler " + handler.__qualname__ + " for path " + path +                                " dosen't exist inside controllers. Do you registry route corectly ?")    def matchController(self, controllers, handler):        for controller in controllers:            if inspect.getmodule(controller) == inspect.getmodule(handler):                return controller        return None