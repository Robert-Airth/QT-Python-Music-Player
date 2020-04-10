import sys
import os
from PySide2.QtUiTools import QUiLoader #allows us to import .ui files
from PySide2.QtWidgets import QApplication, QLineEdit, QPushButton, QRadioButton, QProgressBar, QCheckBox, QSlider, QLabel, QListWidget, QFileDialog, QAction
from PySide2.QtCore import QFile, QObject, QUrl, QTime
from PySide2.QtMultimedia import QMediaPlayer,QMediaPlaylist, QMediaContent



class MainWindow(QObject):

    #class constructor
    def __init__(self, ui_file, parent=None):

        #reference to our music player
        self.music_player = QMediaPlayer()
        self.music_player.setVolume(50)
        

        #call parent QObject constructor
        super(MainWindow, self).__init__(parent)

        #load the UI file into Python
        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.window = loader.load(ui_file)
        
        #always remember to close files
        ui_file.close()

        #add playlist object
        self.playlist = QMediaPlaylist()
        self.playlist.setPlaybackMode(QMediaPlaylist.Sequential)
        self.music_player.setPlaylist(self.playlist)
        self.music_player.setNotifyInterval(50)

        #add a listener to change audio filename displayed
        

        #add playlist display object
        self.playlistDisplay = self.window.findChild(QListWidget, 'PlayListWidget')
        #self.playlist.setPlaybackMode(QMediaPlaylist.CurrentItemOnce)
        #self.playlist.setPlaybackMode(QMediaPlaylist.CurrentItemInLoop)
        #self.playlist.setPlaybackMode(QMediaPlaylist.Random)
        #self.playlist.setPlaybackMode(QMediaPlaylist.Loop)


        #add event listeners
        self.add_media_action = self.window.findChild(QAction, 'action_add_media')
        self.add_media_action.triggered.connect(self.add_media_triggered)

        self.quit_action = self.window.findChild(QAction, 'action_quit')
        self.quit_action.triggered.connect(self.quit_action_triggered)

        self.NextButton = self.window.findChild(QPushButton, 'NextButton')
        self.NextButton.clicked.connect(self.next_button_clicked)

        self.PauseButton = self.window.findChild(QPushButton, 'PauseButton')
        self.PauseButton.clicked.connect(self.pause_button_clicked)
        
        #PlayAllRadioButton = self.window.findChild(QRadioButton, 'PlayAllRadioButton')
        #PlayAllRadioButton.clicked.connect(self.play_all_button_clicked)
        
        self.PlayButton = self.window.findChild(QPushButton, 'PlayButton')
        self.PlayButton.clicked.connect(self.play_button_clicked)
        
        self.PreviousButton = self.window.findChild(QPushButton, 'PreviousButton')
        self.PreviousButton.clicked.connect(self.previous_button_clicked)
        
        #ProgressBar = self.window.findChild(QProgressBar, 'ProgressBar')
        #ProgressBar.valueChanged.connect(self.progress_bar_moved)
        
        self.RepeatOnceRadioButton = self.window.findChild(QRadioButton, 'RepeatOnceRadioButton')
        self.RepeatOnceRadioButton.clicked.connect(self.repeat_once_button_clicked)
        
        
        self.RepeatRadioButton = self.window.findChild(QRadioButton, 'RepeatRadioButton')
        self.RepeatRadioButton.clicked.connect(self.repeat_button_clicked)

        #ShuffleCheckBox = self.window.findChild(QCheckBox, 'ShuffleCheckBox')
        #ShuffleCheckBox.clicked.connect(self.shuffle_checkbox_clicked)

        #ShuttleSlider = self.window.findChild(QSlider, 'ShuttleSlider')
        #ShuttleSlider.valueChanged.connect(self.shuttle_slider_moved)

        self.VolumeSlider = self.window.findChild(QSlider, 'VolumeSlider')
        self.VolumeSlider.setValue(50)
        self.VolumeSlider.valueChanged.connect(self.change_volume_level)

        self.ProgressBar = self.window.findChild(QProgressBar, 'ProgressBar')
        self.music_player.durationChanged.connect(self.progress_bar_maximum_changed)
        self.music_player.positionChanged.connect(self.progress_bar_position_changed)



    

        #self.Playlist = self.window.findChild(QMediaPlaylist, 'Playlist')
        #self.Playlist.itemDoubleClicked.connect(self.volume_slider_moved)



        #show window to user
        self.window.show()


    #I referenced code from Jordan Abbott to complete this function
    def add_media_triggered(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(None,"Select Media Files", "","All Files (*)", options=options)
        if files:
            for file in files:
                self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(file)))
                self.playlistDisplay.addItem(os.path.basename(file))

    def quit_action_triggered(self):
        self.window.close()

    def pause_button_clicked(self):
        self.music_player.pause()

    def next_button_clicked(self):
        if self.music_player.currentMedia().isNull():
            self.playlist.setCurrentIndex(1)
            self.music_player.play()
        else:
            self.playlist.next()

        
    #def play_all_button_clicked(self):
        #
    
    def play_button_clicked(self):
        if self.music_player.currentMedia().isNull():
            self.playlist.setCurrentIndex(1)
            self.next_button_clicked()
            self.music_player.play()
        else:
            self.music_player.play()

        print(QMediaPlayer.EndOfMedia)
        
    
    def previous_button_clicked(self):
        self.playlist.previous()

    def progress_bar_maximum_changed(self, maximum):
        self.ProgressBar.setMaximum(maximum)
       # = self.music_player.duration()

    #def durationChanged(self, duration):
     #   self.positionSlider.setRange(0, duration)


    def progress_bar_position_changed(self, position):
        self.ProgressBar.setValue(position)

    def repeat_once_button_clicked(self, status):
        self.playlist.setPlaybackMode(QMediaPlaylist.CurrentItemOnce)
        self.play_button_clicked()
        self.RepeatOnceRadioButton.setAutoExclusive(False)
        self.RepeatOnceRadioButton.setChecked(False)
        self.RepeatOnceRadioButton.setAutoExclusive(True)
    

    def repeat_button_clicked(self):
        self.playlist.setPlaybackMode(QMediaPlaylist.CurrentItemLoop)

    #def shuffle_checkbox_clicked(self):
        #add code

    #def shuttle_slider_moved(self):
        #add code

    def change_volume_level(self):
        self.music_player.setVolume(self.VolumeSlider.value())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow('MainWindow.ui')
    sys.exit(app.exec_())
