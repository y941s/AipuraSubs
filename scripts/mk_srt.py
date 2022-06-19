import datetime
import pathlib

"""
sample line:

[message text=ああ、一晩考えたんだけど、愛の魅力をもっとみんなに name={user} thumbnial=img_chr_adv_koh-00 clip=\{"_startTime":5.5,"_duration":4.566666666666667,"_easeInDuration":0.0,"_easeOutDuration":0.0,"_blendInDuration":-1.0,"_blendOutDuration":-1.0,"_mixInEaseType":1,"_mixOutEaseType":1,"_timeScale":1.0\}]
"""

def filter_item(items: list[str, ...], key: str) -> str:
    return next((item for item in items if item.startswith(key)), "=")

def evaluate_dict(string: str) -> dict:
    return eval(string.replace("\\", ""))

def parse_message(line: str) -> tuple[str, str, str]:
    items = line.strip("[]\n").split(" ")

    text = filter_item(items, "text").split("=")[1]
    clip = filter_item(items, "clip").split("=")[1]

    if clip != "":
        clip_eval = evaluate_dict(clip)

        start_time = datetime.timedelta(seconds=clip_eval["_startTime"])
        duration = datetime.timedelta(seconds=clip_eval["_duration"])
        end_time = (datetime.datetime.min + start_time + duration).time()
        start_time = (datetime.datetime.min + start_time).time()

        format_string = "%H:%M:%S,%f"
        return (text, start_time.strftime(format_string)[:-3], end_time.strftime(format_string)[:-3])
    return (text, "00:00:00,000", "00:00:00,000")

if __name__ == "__main__":
    raw_dir = pathlib.Path("../adv/")
    target_dir = pathlib.Path("../srt/")

    for raw_file in raw_dir.iterdir():
        timeline = []
        for line in raw_file.open().readlines():
            if line.startswith("[message"):
                timeline.append(parse_message(line))
        
        events = [
            "{}\n{} --> {}\n{}".format(sequence+1, start_time, end_time, text)
            for sequence, (text, start_time, end_time)
            in enumerate(timeline)
        ]

        target_file = target_dir.joinpath("{}.srt".format(raw_file.stem))
        target_file.touch(exist_ok=True)
        target_file.write_text("\n\n".join(events), encoding="utf-8")
