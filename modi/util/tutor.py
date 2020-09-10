import os
import time

from textwrap import fill
from textwrap import dedent


class Tutor:
    row_len = 79

    def __init__(self):
        self.bundle = None
        self.led = None
        self.button = None

    @staticmethod
    def clear():
        clear_cmd = 'cls' if os.name == 'nt' else 'clear'
        os.system(clear_cmd)

    def print_wrap(self, msg):
        message = fill(dedent(msg), self.row_len).lstrip()
        print(message)

    def print_lesson(self, lesson, title):
        print('-' * self.row_len)
        topic = f"Lesson {lesson}: {title}"
        print(f"{topic:^{self.row_len}}")
        print('-' * self.row_len)

    @staticmethod
    def check_user_input(answer, give_answer=True, guide=">>> "):
        response = input(guide)
        nb_wrong = 1
        while response != answer:
            if give_answer:
                print(f"Write below code precisely.\n>>> {answer}\n")
            elif nb_wrong > 2:
                print(f"The answer is {answer}. Type it below.")
            else:
                print("Try again!")
            response = input(guide)
            nb_wrong += 1
        return response

    def run_introduction(self):
        self.clear()
        print("=" * self.row_len)
        print(f"= {'Welcome to the PyMODI Tutor':^{self.row_len - 4}} =")
        print("=" * self.row_len)

        self.print_wrap(
            """
            PyMODI is a very powerful tool that can control the MODI modules
            using python scripts. As long as you learn how to use built-in
            functions of PyMODI, you can easily control MODI modules. This
            interactive CUI tutorial will guide you through the world of PyMODI.
            """
        )

        selection = dedent(
            """
            Tutorial includes:
            1. Making MODI
            2. Accessing Modules
            3. Controlling Modules
            4. Your First PyMODI Project
            """
        )
        print(selection)

        lesson_nb = int(input("Enter the lesson number and press ENTER: "))
        self.clear()

        if not (0 < lesson_nb < 5):
            print("ERROR: lesson_nb must be one of 1, 2, 3 or 4")
            os._exit(0)

        # Skip lesson 1
        if lesson_nb > 1:
            import modi
            print("Preparing the MODI module...")
            input(
                "Connect buttton and led module to your device and press ENTER"
            )
            self.bundle = modi.MODI()

        # Skip lesson 2
        if lesson_nb > 2:
            self.led = self.bundle.leds[0]
            self.button = self.bundle.buttons[0]

        run_selected_lesson = {
            1: self.run_lesson1,
            2: self.run_lesson2,
            3: self.run_lesson3,
            4: self.run_lesson4,
        }.get(lesson_nb)
        run_selected_lesson()

    def run_lesson1(self):
        self.print_lesson(1, "Making MODI")
        self.print_wrap('First, you should import modi. Type "import modi"')

        self.check_user_input('import modi')
        import modi
        print("\nGreat! Now you can use all the features of MODI!\n")

        self.print_wrap(
            """
            To control the modules, make a MODI object that contains all the
            connected modules. Once you create it, it will automatically find
            all the modules connected to the network module.
            """
        )
        input("\nPress ENTER")
        self.clear()

        self.print_wrap(
            """
            Now, prepare real MODI modules. Connect a network module to your
            computing device. Then, connect a Button module and an Led module.
            Make a MODI bundle object by typing bundle = modi.MODI()
            """
        )
        self.check_user_input('bundle = modi.MODI()')
        bundle = modi.MODI()

        self.print_wrap(
            """
            Great! The "bundle" is your MODI object. With it, you can control
            all the modules connected to your device.
            """
        )
        input("\nYou have completed this lesson. Press ENTER to continue")
        self.bundle = bundle

        self.run_lesson2()

    def run_lesson2(self):
        self.clear()
        self.print_lesson(2, "Accessing modules")
        self.print_wrap(
            """
            In the previous lesson, you created a MODI object. Let's figure out
            how we can access modules connected to it.
            """
        )
        print()
        self.print_wrap(
            """
            "bundle.modules" is a method to get all the modules connected to
            the device.
            Type: bundle.modules
            """
        )
        self.check_user_input("bundle.modules")
        print(self.bundle.modules)
        print()

        self.print_wrap(
            """
            You can see two modules connected to the device. You can access
            each module by the same method we use with an array.
            """
        )
        self.print_wrap(
            """
            You can also access modules by types.
            Type: bundle.leds
            """
        )

        self.check_user_input('bundle.leds')
        print(self.bundle.leds)
        print()
        self.print_wrap(
            """
            If you have followed previous instructions correctly, there must be
            one led module connected to the network module. Now, make an led
            variable by accessing the first led module.
            Type: led = bundle.leds[0]
            """
        )

        self.check_user_input('led = bundle.leds[0]')
        led = self.bundle.leds[0]
        self.led = led
        print()
        self.print_wrap(
            """
            Super! You can now do whatever you want with these modules. If you
            have different modules connected, you can access the modules in a
            same way, just typing bundle.<module_name>s"
            """
        )

        input("\nYou have completed this lesson. Press ENTER")

    def run_lesson3(self):
        self.clear()
        self.print_lesson(3, "Controlling modules")
        self.print_wrap("Now you know how to access individual modules. \n"
                        "Let's make an object named \"button\" as well for "
                        "your button module. You know how to do it.")

        self.check_user_input('button = bundle.buttons[0]', False)
        button = self.bundle.buttons[0]
        self.button = button
        print()

        self.print_wrap("Perfect. With your button module and led module, "
                        "we can either get data from the module or send "
                        "command to the module")

        self.print_wrap('get_pressed is a method of a button module which '
                        'returns whether the button is pressed or note.'
                        '\nCheck the state of button by typing'
                        ' button.get_pressed()')

        self.check_user_input('button.get_pressed()')
        print(button.get_pressed())
        print()

        self.print_wrap("Now see if the same command returns True when "
                        "pressing the button.")

        self.check_user_input('button.get_pressed()')
        print(button.get_pressed())
        print()

        self.print_wrap("Good. Now, let's send a command to the led.\n"
                        "set_rgb() is a method of an led module. Let there be "
                        "light by typing led.set_rgb(0, 0, 255)")

        response = self.check_user_input('led.set_rgb(0, 0, 255)')
        exec(response)
        print()

        self.print_wrap("Perfect! You will see the blue light from the "
                        "led module.")

        input("\nYou have completed this lesson.\nPress ENTER")

    def run_lesson4(self, bundle, led, button):
        self.clear()
        self.print_lesson(4, "Your First PyMODI Project")
        self.print_wrap("Let's make a project that blinks led when button "
                        "is pressed.")
        self.print_wrap("In an infinite loop, we want our led to light up "
                        "when button is pressed, and turn off when not "
                        "pressed. Complete the following code based on the"
                        " description.")

        input("\nPress ENTER when you're ready!")
        self.clear()
        print(">>> while True:")
        print("...     # Check if button is pressed")
        self.check_user_input('button.get_pressed():', give_answer=False,
                              guide="...     if ")
        print("...         # Set Led color to green")
        self.check_user_input('led.set_rgb(0, 255, 0)', give_answer=False,
                              guide="...         ")
        print("...     elif button.get_double_clicked():")
        print("...         break")
        print("...     else:")
        print("...         # Turn off the led. i.e. set color to (0, 0, 0)")
        self.check_user_input('led.set_rgb(0, 0, 0)', give_answer=False,
                              guide="...         ")

        self.print_wrap("Congrats!! Now let's see if the code works as we "
                        "want.\nPress the button to light up the led. Double "
                        "click the button to break out of the loop")

        while True:
            if button.get_pressed():
                led.set_rgb(0, 255, 0)
            elif button.get_double_clicked():
                break
            else:
                led.set_off()
            time.sleep(0.02)

        self.print_wrap("\nIt looks great! "
                        "Now you know how to use PyMODI to control modules."
                        "\nYou can look up more functions at "
                        "pymodi.readthedocs.io/en/latest\n"
                        )

        input("\nYou have completed the tutorial.\nPress ENTER to exit")
        self.bundle._com_proc.terminate()
