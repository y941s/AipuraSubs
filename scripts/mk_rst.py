import pathlib

"""
[message text=ああ、一晩考えたんだけど、愛の魅力をもっとみんなに name={user} thumbnial=img_chr_adv_koh-00 clip=\{"_startTime":5.5,"_duration":4.566666666666667,"_easeInDuration":0.0,"_easeOutDuration":0.0,"_blendInDuration":-1.0,"_blendOutDuration":-1.0,"_mixInEaseType":1,"_mixOutEaseType":1,"_timeScale":1.0\}]
"""

if __name__ == "__main__":
    raw_dir = pathlib.Path("../adv/")
    tgt_dir = pathlib.Path("../rst/")
    print(pathlib.Path(".").resolve())

    # for raw_fs in raw_dir.iterdir():
    #     print(raw_fs.name)