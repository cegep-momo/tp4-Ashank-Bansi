from controler.controler import Controler

class Main:
    def __init__(self):
        self.app = Controler()

    def run(self):
        try:
            self.app.boucle()
        finally:
            self.app.fin_programme()

if __name__ == "__main__":
    main = Main()
    main.run()
