import os
import time
import streamlit as st
import numpy as np
from PIL import Image
import datetime


class ExperimentApp:
    def __init__(self):
        # Set default paths
        self.image_path = "/Users/zhangpengfei/PycharmProjects/StreamProject/Imag"
        self.code_path = "/Users/zhangpengfei/PycharmProjects/StreamProject/Code"
        self.logs_path = "/Users/zhangpengfei/PycharmProjects/StreamProject/Logs"
        # self.log_file_path = "D:/Pycharm2024/PyCharm 2024.1/Project/StreamProject/Experiment_Logs.txt"

        self.path_list = [self.image_path, self.code_path, self.logs_path]

        self.state_list = ['Edge Experiment Logs', 'Start Edge']
        self.state = None
        self.program_state = 'None'
        self.search_state = 'None'

        self.image_files = []
        self.image_files_name = []

        self.code_files = []
        self.code_files_name = []

        self.view_day = []
        self.folder_list = []
        self.list_file = []

    def select_time(self):
        st.markdown("# ·Experiment Date")
        self.day = st.date_input(
            label='Experiment Date',
            value=None,
            min_value=None,
            max_value=datetime.date.today(),
            help='Choose the experiment date'
        )

        try:
            if st.button("Create"):
                self.state = self.state_list[1]
                self.program_state = 'view pre log'
                for path in self.path_list:
                    os.chdir(path)
                    file_name = str(self.day)
                    os.makedirs(file_name)
                st.success('Successful Create')
        except Exception as e:
            st.info("The File already exists")

    def enter_text(self):
        st.markdown("# ·Experiment Logs")
        text = st.text_area(
            label='Experiment Logs',
            value='',
            height=150,
            max_chars=2000,
            help='Write your experiment logs here (max 2000 characters)'
        )

        try:
            if st.button('Save'):
                with open(f"D:/Pycharm2024/PyCharm 2024.1/Project/"
                          f"StreamProject/Logs/{str(self.day)}/{str(self.day)}.txt", "w") as f:
                    f.write(text)
                st.success('Successful Save')
            elif text:
                st.warning('The Logs are not Saved')
        except Exception as e:
            pass

    def upload_image(self):
        st.markdown("# ·Experiment Result")
        self.image_files = st.file_uploader(
            "Upload images",
            accept_multiple_files=True,
            type=["jpg", "png", "jpeg"]
        )

        if not self.image_files:
            return None

        for i in range(0, len(self.image_files)):
            self.image_files_name.append(self.image_files[i].name)
            o_img = Image.open(self.image_files[i])
            o_img = np.array(o_img)

            st.text("Result Image:")
            st.image([o_img])

    def save_images(self, image_files, image_name):
        for i in range(0, len(image_files)):
            try:
                img = Image.open(image_files[i])
                img.convert('RGB')
                img_path = os.path.join(f"D:/Pycharm2024/PyCharm 2024.1/Project/"
                                        f"StreamProject/Imag/{str(self.day)}", f"{self.day}_{image_name[i]}.png")
                img.save(img_path)
            except Exception as e:
                st.error(f"Error saving image：{e}")
        st.success('Successful Save Image')

    def upload_code(self):
        st.markdown("# ·Experiment Code")
        code_files = st.file_uploader(
            "Upload Python files",
            accept_multiple_files=True,
            type=["py"]
        )

        if code_files:
            for i, code_file in enumerate(code_files):
                self.code_files_name.append(code_file.name)
                try:
                    code_content = code_file.read().decode("utf-8", errors="ignore")
                    self.code_files.append(code_content)
                    st.code(code_content, language='python')
                except Exception as e:
                    st.error(f"Error reading code file {i + 1}: {str(e)}")

    def save_code(self, code_files, code_name):
        save_dir = f"D:/Pycharm2024/PyCharm 2024.1/Project/StreamProject/Code/{str(self.day)}"

        for i in range(0, len(code_files)):
            try:
                code_content = code_files[i]

                file_path = os.path.join(save_dir, code_name[i])

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(code_content)
                self.process_file(file_path)
                self.process_file(file_path)
            except Exception as e:
                pass
        st.success('Successful Save code')

    def submit_save(self):
        if st.button("Submit & Save"):
            progress_bar = st.sidebar.progress(0)
            status_text = st.sidebar.empty()
            last_rows = np.random.randn(1, 1)

            for i in range(1, 101):
                new_rows = last_rows[-1, :] + np.random.randn(3, 1).cumsum(axis=0)
                status_text.text("Complete: %i%%" % i)

                progress_bar.progress(i)
                last_rows = new_rows
                time.sleep(0.01)

            progress_bar.empty()
            self.save_images(self.image_files, self.image_files_name)
            self.save_code(self.code_files, self.code_files_name)

            self.program_state = 'viewable'

    def file_name(self, file_path):
        file_list = []
        for root, dirs, files in os.walk(file_path):
            # print(root)
            self.folder_list.append(dirs)
            file_list.append(files)

        return file_list

    def show_logs(self, logs_path, list_folder, list_file):
        st.write('· Experiment Logs:')
        if not list_file:
            st.write('None')
        else:
            with open(logs_path + '/' + list_folder + '/' + list_file[0], "r",
                      encoding='GBK') as f:
                data = f.read()
                if data == '':
                    st.write('The log was not edited')
                else:
                    st.write(data)

    def show_image(self, list_folder, list_image):
        st.write('· Experiment Result:')
        if not list_image:
            st.write('None')
        else:
            for i in range(0, len(list_image)):
                image = Image.open(self.image_path + '/' + list_folder + '/' + list_image[i])
                st.image(image, caption=list_image[i])

    def process_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.read().splitlines()

        # 定义去除非空元素后一个紧跟的空字符串的函数
        def remove_empty_after_non_empty(lines):
            new_lines = []
            skip = False  # 用于跳过下一个元素
            for i in range(len(lines)):
                if skip:
                    skip = False
                    continue
                if lines[i] != '':
                    new_lines.append(lines[i])
                    if i + 1 < len(lines) and lines[i + 1] == '':
                        skip = True
                else:
                    new_lines.append(lines[i])
            return new_lines

        new_lines = remove_empty_after_non_empty(lines)

        with open(file_path, 'w', encoding='utf-8') as f:
            for line in new_lines:
                f.write(line + '\n')

    def show_code(self, list_folder, list_code):
        st.write('· Experiment Code:')
        if not list_code:
            st.write('None')
        else:
            for i in range(0, len(list_code)):
                code_path = self.code_path + '/' + list_folder + '/' + list_code[i]
                # self.process_file(code_path)
                with open(code_path, "r", encoding='UTF-8') as code_file:
                    code_content = code_file.read()
                    code_content.splitlines()
                    st.code(code_content, language='python')

    def view_logs(self):
        st.markdown("# ·View_Experiment_Logs")

        log_file_list = self.file_name(self.logs_path)
        list_folder = list(filter(lambda x: x != [], self.folder_list))
        list_folder[0].reverse()
        log_file_list.remove(log_file_list[0])
        list_log_file = log_file_list
        list_log_file.reverse()

        image_file_list = self.file_name(self.image_path)
        image_file_list.remove(image_file_list[0])
        list_image_file = image_file_list
        list_image_file.reverse()

        code_file_list = self.file_name(self.code_path)
        code_file_list.remove(code_file_list[0])
        list_code_file = code_file_list
        list_code_file.reverse()

        for i in range(0, len(list_folder[0])):
            with st.expander(str(list_folder[0][i])):
                self.show_logs(self.logs_path, list_folder[0][i], list_log_file[i])
                self.show_image(list_folder[0][i], list_image_file[i])
                self.show_code(list_folder[0][i], list_code_file[i])

                st.button("Delete", key=f"{i}")

    def view_pre_log(self):
        st.markdown("# ·View_Experiment_Logs")

        log_file_list = self.file_name(self.logs_path)
        list_folder = list(filter(lambda x: x != [], self.folder_list))
        list_folder[0].reverse()
        list_folder[0].pop(0)
        log_file_list.remove(log_file_list[0])
        list_log_file = log_file_list
        list_log_file.reverse()
        list_log_file.pop(0)

        image_file_list = self.file_name(self.image_path)
        image_file_list.remove(image_file_list[0])
        list_image_file = image_file_list
        list_image_file.reverse()
        list_image_file.pop(0)

        code_file_list = self.file_name(self.code_path)
        code_file_list.remove(code_file_list[0])
        list_code_file = code_file_list
        list_code_file.reverse()
        list_code_file.pop(0)

        for i in range(0, len(list_folder[0])):
            with st.expander(str(list_folder[0][i])):
                self.show_logs(self.logs_path, list_folder[0][i], list_log_file[i])
                self.show_image(list_folder[0][i], list_image_file[i])
                self.show_code(list_folder[0][i], list_code_file[i])

                st.button("Delete", key=f"{i}")

    def search_show_logs(self, day):
        file_list = os.listdir(self.logs_path + '/' + day)
        list_log_file = [f for f in file_list
                         if os.path.isfile(os.path.join(self.logs_path + '/' + day, f))]

        image_list = os.listdir(self.image_path + '/' + day)
        list_image_file = [f for f in image_list
                           if os.path.isfile(os.path.join(self.image_path + '/' + day, f))]

        code_list = os.listdir(self.code_path + '/' + day)
        list_code_file = [f for f in code_list
                          if os.path.isfile(os.path.join(self.code_path + '/' + day, f))]

        with st.expander(day):
            self.show_logs(self.logs_path, day, list_log_file)
            self.show_image(day, list_image_file)
            self.show_code(day, list_code_file)

    def batch_search_log(self, path, day):
        try:
            path_list = next(os.walk(path))[1]
            path_list.reverse()
            index = path_list.index(day)

            start_index = max(0, index - 3)
            end_index = min(len(path_list), index + 4)

            result = path_list[start_index:end_index]
            for i in range(0, len(result)):
                self.search_show_logs(result[i])
        except Exception as e:
            st.warning('The date does not exist')

    def search_logs(self):
        try:
            st.markdown("# ·Search Experiment Logs")
            day = st.date_input(
                label='Search Date',
                value=None,
                min_value=None,
                max_value=datetime.date.today(),
                help='Choose the experiment date'
            )

            if st.checkbox('Batch lookup'):
                self.search_state = 'Batch lookup'
            if st.checkbox('Generate keywords'):
                self.search_state = 'Batch lookup'
            # countries = st.multiselect(
            #     "Search Key", ["China", "United States of America"]
            # )

            if st.button('Search'):
                if self.search_state == 'Batch lookup':
                    self.batch_search_log(self.logs_path, str(day))
                else:
                    self.search_show_logs(str(day))
        except Exception as e:
            st.warning('The date does not exist')

    def run(self):
        edge_experiment_logs, search_experiment_logs, view_experiment_logs = st.tabs(
            ["𝐄𝐝𝐠𝐞 𝐄𝐱𝐩𝐞𝐫𝐢𝐦𝐞𝐧𝐭 𝐋𝐨𝐠𝐬", "𝐒𝐞𝐚𝐫𝐜𝐡 𝐄𝐱𝐩𝐞𝐫𝐢𝐦𝐞𝐧𝐭 𝐋𝐨𝐠𝐬", "𝐕𝐢𝐞𝐰 𝐄𝐱𝐩𝐞𝐫𝐢𝐦𝐞𝐧𝐭 𝐋𝐨𝐠𝐬"]
        )

        with edge_experiment_logs:

            self.state = self.state_list[0]

            self.select_time()
            self.enter_text()
            self.upload_image()
            self.upload_code()

            st.sidebar.header(self.state)
            self.submit_save()
        with search_experiment_logs:
            self.search_logs()

        with view_experiment_logs:
            if self.program_state == 'viewable':
                self.view_logs()
            elif self.program_state == 'view pre log':
                self.view_pre_log()
            elif self.program_state == 'None':
                self.view_logs()


if __name__ == '__main__':
    app = ExperimentApp()
    app.run()
