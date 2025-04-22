import streamlit as st
import datetime
import shutil
import time
import os


class LiteratureAPP:
    def __init__(self):
        self.literature = "/Users/zhangpengfei/PycharmProjects/StreamProject/literature"
        self.folder_list = []
        self.category_list = []
        self.file_name = None
        self.uploaded_file = None
        self.literature_day = None
        self.literature_text = None

    def get_all_subfolders(self):
        subfolders = [f.name for f in os.scandir(self.literature) if f.is_dir()]
        self.folder_list = subfolders

    def creat_folder(self):

        st.sidebar.header("Creat Folder")
        folder_name = st.sidebar.text_input('New Folder Name: ')

        if st.sidebar.button('YES'):
            self.get_all_subfolders()
            if folder_name == '':
                warning_empty = st.sidebar.empty()
                warning_empty.warning('The folder name cannot be empty')

                time.sleep(2)
                warning_empty.empty()
            elif folder_name in self.folder_list:
                warning_exist = st.sidebar.empty()
                warning_exist.warning('The folder name already exists')

                time.sleep(2)
                warning_exist.empty()
            else:
                os.chdir(self.literature)
                os.makedirs(str(folder_name))
                st.rerun()

        st.sidebar.header("Edit Folder")
        edit_object = st.sidebar.selectbox('Choose edit object', self.folder_list)
        if st.sidebar.button('Delete'):
            os.chdir(self.literature)
            try:
                shutil.rmtree(str(edit_object))
                st.rerun()
            except Exception as e:
                warning_folder = st.sidebar.empty()
                warning_folder.warning('The folder has been deleted')

                time.sleep(2)
                warning_folder.empty()

    def select_folder(self):
        st.subheader('Choose folder')
        category = st.multiselect(
            " ", self.folder_list
        )

        self.category_list = category

    def submit_save_pdf(self):
        st.subheader('Submit PDF Document')
        self.uploaded_file = st.file_uploader(" ", type="pdf")

    def select_literature_time(self):
        st.subheader('Choose literature time')
        self.literature_day = st.date_input(
            label='',
            value=None,
            min_value=None,
            max_value=datetime.date.today()
        )

    def enter_literature_text(self):
        st.subheader('literature introduce')
        self.literature_text = st.text_area(
            label='',
            value='',
            height=300,
            max_chars=2000
        )

    def sumbit_save(self):
        self.creat_folder()
        self.select_folder()
        st.divider()
        self.submit_save_pdf()
        st.divider()
        self.select_literature_time()
        st.divider()
        self.enter_literature_text()

        if st.button('Submit'):
            if self.uploaded_file is not None:
                self.file_name = self.uploaded_file.name[:-3]

                for file_folder in self.category_list:
                    file_path = self.literature + '/' + file_folder
                    os.chdir(file_path)
                    os.makedirs(self.file_name)

    def run(self):
        self.get_all_subfolders()
        submit_literature, search_literature, view_literature = st.tabs(
            ["Submit Literature", "Search Literature", "View Literature"]
        )
        with submit_literature:
            st.title("Literature upload")
            self.sumbit_save()

        with search_literature:
            pass

        with view_literature:
            pass


if __name__ == '__main__':
    app = LiteratureAPP()
    app.run()

# full_path = os.path.join(self.literature, self.file_name)
# if st.button('Submit'):
#     with open(full_path, "wb") as f:
#         f.write(uploaded_file.getbuffer())
#     st.success('Successful Submit')
