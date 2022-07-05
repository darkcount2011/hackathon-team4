class EnvironmentVariables:
    ENV_PATH = ".env"

    @staticmethod
    def load():
        variables = {}
        for line in EnvironmentVariables.read_file(EnvironmentVariables.ENV_PATH).splitlines():
            if line.startswith("#"):
                continue
            if "=" not in line:
                continue
            k, v = line.split("=", 1)
            variables[k] = v
        return variables

    @staticmethod
    def read_file(file_name):
        with open(file_name, "r") as f:
            return f.read()