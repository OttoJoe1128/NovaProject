class UserInput:
    def __init__(self, memory_core):
        self.memory = memory_core

    def take_input(self):
        user_text = input("Bir şeyler yazın: ")
        self.memory.remember("user_input", user_text)
        print(f"Yazdığınız metin kaydedildi: {user_text}")

    def recall_input(self):
        user_text = self.memory.recall("user_input")
        if user_text:
            print(f"Hatırladığınız metin: {user_text}")
        else:
            print("Hiçbir metin hatırlanmıyor.")
