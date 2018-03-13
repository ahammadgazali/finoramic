import pip


class PackageInstallerClass(object):
   

    def __init__(self):
        self.json_file_txt_path = "/home/kolukuri/Videos/analytics_regression_Thurs15/analytics_regression/inputs_text.json"

    def parse_input_file_fn(self):
        with open(self.json_file_txt_path, 'r') as input_file:
            try:
                json_f = input_file.read()
                json_f = json_f.replace('{', '\n')
                json_f = json_f.replace('}', '\n')
                json_f = json_f.replace(',', '\n')
                return json_f
            except ValueError as e:
                print('invalid json: %s' % e)
                return None

    def main(self):
        output = self.parse_input_file_fn()
        summary_dict = {'success': [], 'fail': []}
        for i in output.splitlines():
            if "==" in i:
                status = pip.main(['install', i])
                print status
                if status == 0:
                    print "%s : Module installed successfully" % i
                    summary_dict['success'].append(i)
                else:
                    print "%s : Module failed to install" % i
                    summary_dict['fail'].append(i)
        print summary_dict
        for k, dependency_list in summary_dict.items():
            print "-"*20, k, " dependencies", "-"*20
            for enum, dependency in enumerate(dependency_list, 1):
                print enum, ". ", dependency


if __name__ == '__main__':
    abc = PackageInstallerClass()
    abc.main()