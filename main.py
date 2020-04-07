import sys
from PySide2.QtUiTools import QUiLoader #allows us to import .ui files
from PySide2.QtWidgets import QApplication, QLineEdit, QPushButton, QRadioButton, QProgressBar, QCheckBox, QSlider, QLabel, QFileDialog, QAction
from PySide2.QtCore import QFile, QObject, QUrl
from PySide2.QtMultimedia import QMediaPlayer

class MainWindow(QObject):

    #class constructor
    def __init__(self, ui_file, parent=None):

        #reference to our music player
        self.music_player = QMediaPlayer()
        self.music_player.setVolume(100)

        #call parent QObject constructor
        super(MainWindow, self).__init__(parent)

        #load the UI file into Python
        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.window = loader.load(ui_file)
        
        #always remember to close files
        ui_file.close()

        #add event listeners
        open_action = self.window.findChild(QAction, 'action_open')
        open_action.triggered.connect(self.open_action_triggered)

        quit_action = self.window.findChild(QAction, 'action_quit')
        quit_action.triggered.connect(self.quit_action_triggered)

        NextButton = self.window.findChild(QPushButton, 'NextButton')
        NextButton.clicked.connect(self.next_button_clicked)

        PauseButton = self.window.findChild(QPushButton, 'PauseButton')
        PauseButton.clicked.connect(self.pause_button_clicked)
        
        PlayAllRadioButton = self.window.findChild(QRadioButton, 'PlayAllRadioButton')
        PlayAllRadioButton.clicked.connect(self.play_all_button_clicked)
        
        PlayButton = self.window.findChild(QPushButton, 'PlayButton')
        PlayButton.clicked.connect(self.play_button_clicked)
        
        PreviousButton = self.window.findChild(QPushButton, 'PreviousButton')
        PreviousButton.clicked.connect(self.previous_button_clicked)
        
        ProgressBar = self.window.findChild(QProgressBar, 'ProgressBar')
        ProgressBar.valueChanged.connect(self.progress_bar_moved)
        
        RepeatOnceRadioButton = self.window.findChild(QRadioButton, 'RepeatOnceRadioButton')
        RepeatOnceRadioButton.clicked.connect(self.repeat_once_button_clicked)
        
        RepeatRadioButton = self.window.findChild(QRadioButton, 'RepeatRadioButton')
        RepeatRadioButton.clicked.connect(self.repeat_button_clicked)

        ShuffleCheckBox = self.window.findChild(QCheckBox, 'ShuffleCheckBox')
        ShuffleCheckBox.clicked.connect(self.shuffle_checkbox_clicked)

        ShuttleSlider = self.window.findChild(QSlider, 'ShuttleSlider')
        ShuttleSlider.valueChanged.connect(self.shuttle_slider_moved)

        VolumeSlider = self.window.findChild(QSlider, 'VolumeSlider')
        VolumeSlider.valueChanged.connect(self.volume_slider_moved)

        Playlist = self.window.findChild(QMediaPlaylist, 'Playlist')
        VolumeSlider.itemDoubleClicked.connect(self.volume_slider_moved)



        #show window to user
        self.window.show()

    def open_action_triggered(self):
        file_name = QFileDialog.getOpenFileName(self.window)

        self.music_player.setMedia(QUrl.fromLocalFile(file_name[0]))

    def quit_action_triggered(self):
        self.window.close()

    def pause_button_clicked(self):
        self.music_player.pause()

    def next_button_clicked(self):
        add = code
        
    def play_all_button_clicked(self):
        add = code
    
    def play_button_clicked(self):
        self.music_player.play()
    
    #def previous_button_clicked(self):
        #add code

    #def progress_bar_moved(self):
        #add code

    #def repeat_once_button_clicked(self):
        #add code

    #def repeat_button_clicked(self):
        #add code

    #def shuffle_checkbox_clicked(self):
        #add code

    #def shuttle_slider_moved(self):
        #add code

    #def volume_slider_moved(self):
        #add code

    #def change_volume_level(self):
        #self.music_player.setVolume(self.vo)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow('MainWindow.ui')
    sys.exit(app.exec_())
