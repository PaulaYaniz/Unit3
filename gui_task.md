# GUI task
![image](https://user-images.githubusercontent.com/89135778/215648403-f841f1ed-87c1-46ff-ac91-a64a6dca9a31.png)

## Currency_Converter_App.py
```.py
# Currency_Converter_App.py
from kivymd.app import MDApp


class currency_converter(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.converted_amount = 0
        self.euros = 0

    def build(self):
        return

    def enter_eur(self):
        if not self.root.ids.user_num.text.isdigit():
            self.root.ids.counter_label.text = f"Please enter a number."
        else:
            number = int(self.root.ids.user_num.text)
            self.euros = number
            self.root.ids.counter_label.text = f"Amount entered is {self.euros} euros."

    def jpy(self):
        # convert eur to jpy
        self.converted_amount = self.euros * 141
        self.root.ids.counter_label.text = f"Amount converted is {round(self.converted_amount, 2)} yen."

    def usd(self):
        # convert eur to usd
        self.converted_amount = self.euros * 1.09
        self.root.ids.counter_label.text = f"Amount converted is {round(self.converted_amount, 2)} dollars."


my_app = currency_converter()
my_app.run()

```

## currency_converter.kv
```.kv
# currency_converter.kv

Screen:
    size: 500, 500
    md_bg_color: "#a3b18a"

    MDBoxLayout:
        id:main_box
        orientation: "vertical"
        size_hint: 1, 1
        pos_hint: {"center_x":.5, "center_y":.5}
        md_bg_color: "#cffcdb"

        MDLabel:
            text:"Currency Converter"
            halign: "center"
            valign: "top"
            font_size: 40
            pos_hint: {"center_x": .5, "center_y": .9}

        MDTextField:
            id:user_num
            hint_text: "Enter an amount in Euros"
            mode: "rectangle"
            size_hint: .7, .5
            pos_hint: {"center_x": .5, "center_y": .5}
            on_text:
                app.enter_eur()

        MDBoxLayout:
            id:second_box
            size_hint: 1, .5
            orientation: "horizontal"
            md_bg_color: "#e6e8a0"

            MDLabel:
                id:counter_label
                text: "    Click to convert"
                font_size: 20
                color: "#283618"
                size_hint: .5, 1

            MDBoxLayout:
                id: third_box
                orientation: "vertical"
                size_hint: .5, 1

                MDRaisedButton:
                    id:jpy_btn
                    text:"JPY"
                    font_size: 30
                    size_hint: .5, 1
                    md_bg_color:"#8fa9f2"
                    on_release:
                        app.jpy()

                MDRaisedButton:
                    id:usd_btn
                    text:"USD"
                    font_size: 30
                    size_hint: .5, 1
                    md_bg_color:"#8fa9f2"
                    on_release:
                        app.usd()

```
## OUTPUT
### Initial view
![image](https://user-images.githubusercontent.com/89135778/215648542-708132e8-9ade-48a8-900a-fc8860c8bde8.png)
### after entering the number
![image](https://user-images.githubusercontent.com/89135778/215648745-6c78168c-bab9-4ba4-b0f3-bb55ee8770f5.png)
### Clicking on jpy, converting to yen
![image](https://user-images.githubusercontent.com/89135778/215648826-9bbb175d-0484-4f00-a2e2-d2fb48cab9be.png)
### Clicking on usd, converting to dollars
![image](https://user-images.githubusercontent.com/89135778/215649046-135805e3-3180-461c-8de7-28bc63e836f5.png)
### Validating user input
![image](https://user-images.githubusercontent.com/89135778/215649173-4e68ee06-211e-44b0-8862-79a9a321604b.png)
