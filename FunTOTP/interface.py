from getpass import getpass
from colorama import init, Fore, Back, Style

yes = ['Y', 'y', 'YES', 'yes', 'Yes']
class interface(object):
    """
    Terminal CLI
    """

    def log(self, arg, get=False):
        if not get:
            print("[*]: {} ".format(arg))
        else:
            return "[*]: {} ".format(arg)

    def error(self, arg, get=False):
        """Short summary.

        Parameters
        ----------
        arg : str
            String to print
        get : bool
            If true, returns a string with the formated string

        Returns
        -------
        str
            If get = true, returns a string with the formated string

        """
        if not get:
            print(Fore.RED + "[ERROR]: {}".format(arg))
            print(Style.RESET_ALL)
            exit(-1)
        else:
            return "[ERROR]: {}".format(arg)

    def warning(self, arg, get=False):
        if not get:
            print(Fore.YELLOW + "[!]: {}".format(arg), end='')
            print(Style.RESET_ALL)
        else:
            return "[!]: {}".format(arg)

    def sure(self):
        user = input(self.log("Are you sure? (y/N) ", get=True))

        if user in yes:
            return 0
        else:
            exit(0)

    def newpasswd(self):
        condition = True
        while condition is True:
            user_psswd = getpass("[*]: Password:")
            user_psswd_repeat = getpass("[*]: Repeat password:")

            if user_psswd == user_psswd_repeat:
                condition = False
            else:
                self.warning("Passwords don't match! Try again")

        return user_psswd_repeat

    def passwd(self):
        return getpass()

    def info(self, arg):
        print(Fore.BLACK + Back.WHITE + "[i]: {}".format(arg) + ' ', end='')
        print(Style.RESET_ALL)
