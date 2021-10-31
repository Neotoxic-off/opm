class Colors:
    def __init__(self):
        self.colors = {
            "reset" : "0",
            "red" : "31",
            "green" : "32",
            "yellow" : "33",
            "blue" : "34",
            "purple" : "35",
            "cyan" : "36",
            "white" : "37"
        }

    def get(self, color):
        if (color in self.colors.keys()):
            return (self.colors[color])
        return (self.colors["reset"])

    def build(self, color):
        return ("\033[{};{}m".format(
            self.get(color),
            1
        ))

class Logs:
    def __init__(self):
        self.colors = Colors()
        self.logs = {
            "action" : "::",
            "success" : "--",
            "error" : "##",
            "warning" : "=="
        }

    def action(self, message):
        self.render(
            self.colors.build("blue"),
            "{} {}{}".format(
                self.logs["action"],
                self.colors.build("reset"),
                message
            )
        )

    def success(self, message):
        self.render(
            self.colors.build("cyan"),
            "   {} {} ".format(
                self.logs["success"],
                message
            )
        )

    def error(self, message):
        self.render(
            self.colors.build("red"),
            "   {} {} ".format(
                self.logs["error"],
                message
            )
        )

    def warning(self, message):
        self.render(
            self.colors.build("yellow"),
            "{} {} ".format(
                self.logs["warning"],
                message
            )
        )

    def render(self, color, message):
        print("{}{}{}".format(
            color,
            message,
            self.colors.build("reset")
        ))
