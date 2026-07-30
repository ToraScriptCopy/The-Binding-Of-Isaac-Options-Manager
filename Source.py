# Ahhh Meow Python Chan~~~
import os
import sys
import ctypes
import winreg
import subprocess
import psutil
import urllib.request
import customtkinter as ctk
from tkinter import filedialog
from PIL import Image

def setup_auto_admin():
    try:
        if not ctypes.windll.shell32.IsUserAnAdmin():
            script_path = os.path.abspath(sys.argv[0])
            key_path = r"Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Layers"
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_WRITE) as key:
                winreg.SetValueEx(key, script_path, 0, winreg.REG_SZ, "~ RUNASADMIN")
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f'"{script_path}"', None, 1)
            sys.exit()
    except Exception:
        pass

setup_auto_admin()

def setup_taskbar_identity():
    try:
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("Meow.Isaac.Panel")
    except Exception:
        pass

setup_taskbar_identity()

def auto_detect_options_ini():
    user_profile = os.environ.get("USERPROFILE", "")
    my_games = os.path.join(user_profile, "Documents", "My Games")
    if os.path.exists(my_games):
        for folder in os.listdir(my_games):
            if "binding of isaac" in folder.lower():
                target = os.path.join(my_games, folder, "options.ini")
                if os.path.exists(target):
                    return target
    return None

def auto_detect_isaac_exe():
    default_steam = r"C:\program files (x86)\steam\steamapps\common\The Binding of Isaac Rebirth\isaac-ng.exe"
    if os.path.exists(default_steam):
        return default_steam
    return None

CONFIG_PATH = auto_detect_options_ini() or r"C:\Users\nikit\Documents\My Games\Binding of Isaac Repentance+\options.ini"
GAME_PATH = auto_detect_isaac_exe() or r"C:\program files (x86)\steam\steamapps\common\The Binding of Isaac Rebirth\isaac-ng.exe"
LUATOOLS_EXE_PATH = r"C:\Users\nikit\AppData\Local\LuaTools\current\LuaTools.exe"

URL_MAIN_ICON = "https://i.pinimg.com/736x/7e/c5/76/7ec576dd62212111f8d1bb8dd1ed877b.jpg"
URL_STEAM = "https://images.icon-icons.com/3053/PNG/512/steam_alt_macos_bigsur_icon_189698.png"
URL_LUATOOLS = "https://status.lua.tools/upload/logo1.png?t=1781052374946"
URL_STEAMRIP = "https://tse2.mm.bing.net/th/id/OIP.g-rZV77ylPx1Mufgj3mjCAAAAA?r=0&rs=1&pid=ImgDetMain&o=7&rm=3"
URL_PIRATES = "https://i.pinimg.com/736x/05/25/f4/0525f46e953b889b4e2c716866247649.jpg"

TEMP_DIR = os.environ.get("TEMP", ".")
IMAGE_CACHE = {}

def load_remote_image(url, filename, size=(16, 16)):
    path = os.path.join(TEMP_DIR, filename)
    if not os.path.exists(path):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=3) as resp, open(path, 'wb') as f:
                f.write(resp.read())
        except Exception:
            return None
    try:
        img = Image.open(path)
        return ctk.CTkImage(light_image=img, dark_image=img, size=size)
    except Exception:
        return None

DESCRIPTIONS = {
    "Language": "Language setting. Warning: changing this in-game config may lead to unstable behavior or crashes.",
    "MusicVolume": "Controls the background music volume level in the game.",
    "MusicEnabled": "Enables or disables background music completely.",
    "SFXVolume": "Controls sound effects volume (shots, enemies, explosions).",
    "MapOpacity": "Adjusts transparency level of the minimap overlay.",
    "Fullscreen": "Toggles between Fullscreen mode and Windowed mode.",
    "Filter": "Applies pixel smoothing filter to game graphics.",
    "Exposure": "Adjusts global visual exposure level.",
    "Gamma": "Gamma is the color brightness rendering balance for dark rooms.",
    "ControllerHotplug": "Allows dynamic controller connection during gameplay.",
    "PopUps": "Shows popup notifications for achievements and items.",
    "CameraStyle": "Switches camera tracking behavior between static and dynamic.",
    "ShowRecentItems": "Configures HUD display mode for recently picked up items.",
    "HudOffset": "Adjusts margin position of HUD elements from screen edges.",
    "TryImportSave": "Attempts to automatically import previous save files.",
    "FoundHUD": "Displays detailed stats on screen (damage, tear rate, speed).",
    "EnableMods": "Globally toggles Steam Workshop and local Lua mods.",
    "RumbleEnabled": "Enables gamepad vibration feedback.",
    "ChargeBars": "Shows charging meters next to player for charged attacks.",
    "BulletVisibility": "Outlines enemy projectiles for increased visibility.",
    "TouchMode": "Enables touch control overlays for compatible devices.",
    "AimLock": "Locks shooting direction relative to movement direction.",
    "JacobEsauControls": "Toggles control scheme options for Jacob and Esau.",
    "AscentVoiceOver": "Enables narration audio during the Ascent route.",
    "OnlineHud": "Displays network status and player indicators in multiplayer.",
    "StreamerMode": "Hides sensitive lobby info and seeds for live streaming.",
    "OnlinePlayerVolume": "Sets voice chat volume for online players.",
    "OnlinePlayerOpacity": "Adjusts transparency for remote player characters.",
    "OnlineChatEnabled": "Toggles text chat overlay in online multiplayer.",
    "OnlineChatFilterEnabled": "Enables profanity filtering for text chat.",
    "MultiplayerColorSet": "Selects custom color palette for player indicators.",
    "OnlineInputDelay": "Adjusts network buffer delay to balance smooth play and lag.",
    "ItemInfoDisplayEnabled": "Shows item descriptions upon pickup.",
    "AcceptedPublicBeta_v1.9.7.17": "Public beta agreement state flag.",
    "AcceptedDataCollectionDisclaimer": "Telemetry disclaimer state flag.",
    "EnableDebugConsole": "Toggles built-in developer debug console (~ key).",
    "MaxScale": "Sets maximum visual scaling factor for game rendering.",
    "MaxRenderScale": "Controls internal render resolution multiplier.",
    "VSync": "Locks framerate to monitor refresh rate to prevent tearing.",
    "PauseOnFocusLost": "Pauses game automatically when switching windows.",
    "SteamCloud": "Syncs save data with Steam Cloud servers.",
    "MouseControl": "Enables targeting and aiming with mouse cursor.",
    "BossHpOnBottom": "Moves boss health bar to bottom of screen.",
    "AnnouncerVoiceMode": "Configures pill/card announcer voice frequency.",
    "ConsoleFont": "Sets font size scale for developer debug console.",
    "FadedConsoleDisplay": "Fades console log text when developer console is idle.",
    "SaveCommandHistory": "Saves previous console commands across sessions.",
    "WindowWidth": "Sets custom window width in pixels.",
    "WindowHeight": "Sets custom window height in pixels.",
    "WindowPosX": "Sets window horizontal screen coordinate position.",
    "WindowPosY": "Sets window vertical screen coordinate position.",
    "UseExclusiveFullscreen": "Forces hardware exclusive fullscreen mode.",
    "EnableEpicOverlay": "Enables Epic Games Store overlay compatibility.",
    "EosCrossplay": "Toggles Epic Online Services crossplay support."
}

DEFAULTS = {
    "Language": ("dropdown", "0", ["0 - English", "1 - Japanese", "2 - Korean", "3 - Chinese", "4 - Russian", "5 - German", "6 - Spanish"]),
    "MusicVolume": ("float", 0.1, 0.0, 1.0, [("Mute (0)", 0.0), ("50%", 0.5), ("Max (1.0)", 1.0)]),
    "MusicEnabled": ("bool", 0),
    "SFXVolume": ("float", 0.7, 0.0, 1.0, [("Mute (0)", 0.0), ("50%", 0.5), ("Max (1.0)", 1.0)]),
    "MapOpacity": ("float", 0.4, 0.0, 1.0, [("Invisible (0)", 0.0), ("Half (0.5)", 0.5), ("Solid (1.0)", 1.0)]),
    "Fullscreen": ("bool", 1),
    "Filter": ("bool", 0),
    "Exposure": ("float", 1.0, 0.0, 3.0, [("Low (0.5)", 0.5), ("Normal (1.0)", 1.0), ("High (2.0)", 2.0)]),
    "Gamma": ("float", 1.15, 0.5, 3.0, [("Night (0.6)", 0.6), ("Normal (1.0)", 1.0), ("Fullbright (2.5)", 2.5)]),
    "ControllerHotplug": ("bool", 1),
    "PopUps": ("bool", 1),
    "CameraStyle": ("int", 1, 0, 5, [("Default (1)", 1), ("Dynamic (2)", 2)]),
    "ShowRecentItems": ("int", 2, 0, 5, [("Off (0)", 0), ("Compact (1)", 1), ("Full (2)", 2)]),
    "HudOffset": ("float", 0.0, 0.0, 1.0, [("Min (0.0)", 0.0), ("Center (0.5)", 0.5), ("Max (1.0)", 1.0)]),
    "TryImportSave": ("bool", 0),
    "FoundHUD": ("bool", 1),
    "EnableMods": ("bool", 1),
    "RumbleEnabled": ("bool", 1),
    "ChargeBars": ("bool", 1),
    "BulletVisibility": ("bool", 1),
    "TouchMode": ("bool", 1),
    "AimLock": ("bool", 1),
    "JacobEsauControls": ("bool", 1),
    "AscentVoiceOver": ("bool", 1),
    "OnlineHud": ("bool", 0),
    "StreamerMode": ("bool", 0),
    "OnlinePlayerVolume": ("int", 6, 0, 10, [("Min (0)", 0), ("Mid (5)", 5), ("Max (10)", 10)]),
    "OnlinePlayerOpacity": ("int", 10, 0, 10, [("Min (0)", 0), ("Mid (5)", 5), ("Max (10)", 10)]),
    "OnlineChatEnabled": ("bool", 1),
    "OnlineChatFilterEnabled": ("bool", 1),
    "MultiplayerColorSet": ("int", 0, 0, 10, []),
    "OnlineInputDelay": ("int", 3, 0, 10, [("1ms", 1), ("3ms", 3), ("5ms", 5)]),
    "ItemInfoDisplayEnabled": ("bool", 1),
    "AcceptedPublicBeta_v1.9.7.17": ("bool", 1),
    "AcceptedDataCollectionDisclaimer": ("bool", 1),
    "EnableDebugConsole": ("bool", 0),
    "MaxScale": ("int", 99, 1, 99, [("Auto (99)", 99), ("1x", 1), ("2x", 2), ("3x", 3)]),
    "MaxRenderScale": ("int", 2, 1, 10, [("1x", 1), ("2x", 2), ("4x", 4)]),
    "VSync": ("bool", 1),
    "PauseOnFocusLost": ("bool", 1),
    "SteamCloud": ("bool", 1),
    "MouseControl": ("bool", 0),
    "BossHpOnBottom": ("bool", 1),
    "AnnouncerVoiceMode": ("int", 0, 0, 5, [("Random (0)", 0), ("Always (1)", 1), ("Never (2)", 2)]),
    "ConsoleFont": ("int", 0, 0, 5, [("Default (0)", 0), ("Large (1)", 1)]),
    "FadedConsoleDisplay": ("bool", 0),
    "SaveCommandHistory": ("bool", 1),
    "WindowWidth": ("window_dim", 1917, 640, 3840),
    "WindowHeight": ("window_dim", 980, 480, 2160),
    "WindowPosX": ("int", 130, 0, 2000, []),
    "WindowPosY": ("int", 130, 0, 2000, []),
    "UseExclusiveFullscreen": ("bool", 0),
    "EnableEpicOverlay": ("bool", 1),
    "EosCrossplay": ("bool", 0)
}

CONSOLE_SETTINGS = ["EnableDebugConsole", "ConsoleFont", "FadedConsoleDisplay", "SaveCommandHistory"]

def read_options():
    options = {}
    if not os.path.exists(CONFIG_PATH):
        return options
    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if "=" in line and not line.startswith("["):
                    key, val = line.split("=", 1)
                    options[key.strip()] = val.strip()
    except Exception:
        pass
    return options

def write_option(key, val):
    if not os.path.exists(CONFIG_PATH):
        os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            f.write("[Options]\n")
            f.write(f"{key}={val}\n")
        return

    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            lines = f.readlines()

        found = False
        new_lines = []
        for line in lines:
            if line.strip().startswith(f"{key}="):
                new_lines.append(f"{key}={val}\n")
                found = True
            else:
                new_lines.append(line)

        if not found:
            new_lines.append(f"{key}={val}\n")

        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
    except Exception:
        pass

def check_game_status():
    isaac_running = False
    spacewar_running = False

    for proc in psutil.process_iter(['name']):
        try:
            name = proc.info['name'].lower() if proc.info['name'] else ""
            if name == "isaac-ng.exe":
                isaac_running = True
            elif name == "spacewar.exe":
                spacewar_running = True
        except Exception:
            pass

    detected_platform = "pirates"
    if os.path.exists(LUATOOLS_EXE_PATH) or spacewar_running:
        detected_platform = "luatools"
    else:
        steamrip_found = False
        game_dir = os.path.dirname(GAME_PATH)
        parent_dir = os.path.dirname(game_dir)
        grandparent_dir = os.path.dirname(parent_dir)

        for d in [game_dir, parent_dir, grandparent_dir]:
            if os.path.exists(d):
                if "steamrip.com" in os.path.basename(d).lower():
                    steamrip_found = True
                    break
                for f in os.listdir(d):
                    if "steamrip" in f.lower():
                        steamrip_found = True
                        break
            if steamrip_found:
                break

        if steamrip_found:
            detected_platform = "steamrip"
        elif "steamapps" in GAME_PATH.lower() and os.path.exists(GAME_PATH):
            detected_platform = "steam"

    return isaac_running, detected_platform

def play_game():
    if os.path.exists(GAME_PATH):
        subprocess.Popen([GAME_PATH], cwd=os.path.dirname(GAME_PATH))

def restart_game():
    for proc in psutil.process_iter(['name']):
        try:
            if proc.info['name'] and proc.info['name'].lower() == "isaac-ng.exe":
                proc.kill()
        except Exception:
            pass
    play_game()

def open_config_file():
    if os.path.exists(CONFIG_PATH):
        os.startfile(CONFIG_PATH)
    else:
        os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            f.write("[Options]\n")
        os.startfile(CONFIG_PATH)

class CustomTooltip:
    def __init__(self, widget, get_text_func, delay=300):
        self.widget = widget
        self.get_text_func = get_text_func
        self.delay = delay
        self.tip_window = None
        self.scheduled_id = None

        self.widget.bind("<Enter>", self.schedule_show)
        self.widget.bind("<Leave>", self.hide_tip)
        self.widget.bind("<ButtonPress>", self.hide_tip)

    def schedule_show(self, event=None):
        self.cancel_schedule()
        self.scheduled_id = self.widget.after(self.delay, self.show_tip)

    def cancel_schedule(self):
        if self.scheduled_id:
            self.widget.after_cancel(self.scheduled_id)
            self.scheduled_id = None

    def show_tip(self, event=None):
        self.scheduled_id = None
        if self.tip_window or not self.get_text_func:
            return
        text = self.get_text_func() if callable(self.get_text_func) else self.get_text_func
        if not text:
            return

        x = self.widget.winfo_rootx() + 20
        y = self.widget.winfo_rooty() + self.widget.winfo_height() + 5

        self.tip_window = tw = ctk.CTkToplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")
        tw.attributes("-topmost", True)

        frame = ctk.CTkFrame(tw, fg_color="#2B2B2B", border_color="#444444", border_width=1, corner_radius=6)
        frame.pack(fill="both", expand=True, padx=2, pady=2)

        lbl = ctk.CTkLabel(frame, text=text, font=("Segoe UI", 11), text_color="#E0E0E0", justify="left", wraplength=260)
        lbl.pack(padx=8, pady=6)

    def hide_tip(self, event=None):
        self.cancel_schedule()
        tw = self.tip_window
        self.tip_window = None
        if tw:
            try:
                tw.destroy()
            except Exception:
                pass

def bind_fast_scroll(scroll_widget):
    canvas = scroll_widget._parent_canvas
    def _on_wheel(event):
        delta = event.delta
        if sys.platform == "darwin":
            canvas.yview_scroll(int(-1 * delta), "units")
        else:
            steps = int(-1 * (delta / 120) * 3)
            canvas.yview_scroll(steps, "units")
    
    def _bind_children(widget):
        widget.bind("<MouseWheel>", _on_wheel, add="+")
        for child in widget.winfo_children():
            _bind_children(child)

    _bind_children(scroll_widget)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("???")
app.geometry("620x700")
app.resizable(False, False)
app.attributes("-topmost", True)

temp_icon_path = os.path.join(TEMP_DIR, "isaac_window_icon.ico")
try:
    req = urllib.request.Request(URL_MAIN_ICON, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=5) as resp:
        img_data = resp.read()
        with open(temp_icon_path, 'wb') as f:
            f.write(img_data)
    img_ico = Image.open(temp_icon_path).convert("RGBA")
    img_ico.save(temp_icon_path, format="ICO", sizes=[(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
    app.iconbitmap(default=temp_icon_path)
    app.wm_iconbitmap(default=temp_icon_path)
except Exception:
    pass

def apply_cat_icon(window):
    try:
        if os.path.exists(temp_icon_path):
            window.iconbitmap(temp_icon_path)
            window.after(150, lambda: window.iconbitmap(temp_icon_path))
    except Exception:
        pass

options_data = read_options()

grid_canvas = ctk.CTkCanvas(app, bg="#181818", highlightthickness=0)
grid_canvas.place(x=0, y=0, relwidth=1.0, relheight=1.0)

def draw_grid_pattern(event=None):
    grid_canvas.delete("all")
    w = app.winfo_width()
    h = app.winfo_height()
    grid_size = 28
    line_color = "#232323"
    for x in range(0, w, grid_size):
        grid_canvas.create_line(x, 0, x, h, fill=line_color, width=1)
    for y in range(0, h, grid_size):
        grid_canvas.create_line(0, y, w, y, fill=line_color, width=1)

grid_canvas.bind("<Configure>", draw_grid_pattern)

header_frame = ctk.CTkFrame(app, fg_color="#181818", height=64, corner_radius=0)
header_frame.pack(fill="x", side="top")

icon_img = load_remote_image(URL_MAIN_ICON, "isaac_main_icon.jpg", size=(50, 50))
if icon_img:
    img_lbl = ctk.CTkLabel(header_frame, image=icon_img, text="")
    img_lbl.pack(side="left", padx=10, pady=5)
    CustomTooltip(img_lbl, "MEOWWW")

title_lbl = ctk.CTkLabel(header_frame, text="Cat Panel", font=("Segoe UI", 20, "bold"), text_color="#FFFFFF")
title_lbl.pack(side="left", padx=(0, 10), pady=10)

status_container = ctk.CTkFrame(header_frame, fg_color="transparent")
status_container.pack(side="right", padx=16, pady=10)

status_dot_canvas = ctk.CTkCanvas(status_container, width=14, height=14, bg="#181818", highlightthickness=0)
status_dot_canvas.pack(side="top", anchor="center")

platform_icon_label = ctk.CTkLabel(status_container, text="")
platform_icon_label.pack(side="top", anchor="center", pady=(4, 0))

IMAGE_CACHE["steam"] = load_remote_image(URL_STEAM, "icon_steam.png", size=(18, 18))
IMAGE_CACHE["luatools"] = load_remote_image(URL_LUATOOLS, "icon_luatools.png", size=(18, 18))
IMAGE_CACHE["steamrip"] = load_remote_image(URL_STEAMRIP, "icon_steamrip.png", size=(18, 18))
IMAGE_CACHE["pirates"] = load_remote_image(URL_PIRATES, "icon_pirates.jpg", size=(18, 18))

current_status_text = ["Game status: Checking..."]
current_platform_text = ["Platform: Checking..."]

CustomTooltip(status_dot_canvas, lambda: current_status_text[0])
CustomTooltip(platform_icon_label, lambda: current_platform_text[0])

def update_game_status_indicator():
    status_dot_canvas.delete("all")
    is_running, platform_type = check_game_status()
    
    current_platform_text[0] = f"Platform: {platform_type.capitalize()}"
    
    if is_running:
        status_dot_canvas.create_oval(1, 1, 13, 13, fill="#4CAF50", outline="")
        current_status_text[0] = "Game status: Running"
    else:
        status_dot_canvas.create_oval(1, 1, 13, 13, fill="#555555", outline="")
        current_status_text[0] = "Game status: Not running"

    if platform_type in IMAGE_CACHE and IMAGE_CACHE[platform_type]:
        platform_icon_label.configure(image=IMAGE_CACHE[platform_type])
    else:
        platform_icon_label.configure(image="")

    app.after(2000, update_game_status_indicator)

nav_frame = ctk.CTkFrame(app, fg_color="#181818", height=40, corner_radius=0)
nav_frame.pack(fill="x", side="top", pady=(0, 10))

nav_inner = ctk.CTkFrame(nav_frame, fg_color="transparent")
nav_inner.pack(anchor="center")

content_container = ctk.CTkFrame(app, fg_color="transparent", corner_radius=0)
content_container.pack(fill="both", expand=True)

pages = {}
current_page_name = [None]
nav_buttons = {}

def create_page(name):
    page = ctk.CTkFrame(content_container, fg_color="transparent", corner_radius=0)
    pages[name] = page
    return page

page_main = create_page("Main")
page_console = create_page("Console Hub")
page_all = create_page("All Settings")

for p in pages.values():
    p.place(relx=0, rely=0, relwidth=1.0, relheight=1.0)

def show_page(name):
    if current_page_name[0] == name:
        return
    
    current_page_name[0] = name
    for btn_name, btn in nav_buttons.items():
        if btn_name == name:
            btn.configure(fg_color="#3A3A3A", text_color="#FFFFFF")
        else:
            btn.configure(fg_color="#2B2B2B", text_color="#AAAAAA")

    pages[name].lift()

for name in ["Main", "Console Hub", "All Settings"]:
    btn = ctk.CTkButton(
        nav_inner,
        text=name,
        width=110,
        height=30,
        font=("Segoe UI", 12, "bold"),
        fg_color="#2B2B2B",
        hover_color="#3A3A3A",
        text_color="#AAAAAA",
        corner_radius=6,
        command=lambda n=name: show_page(n)
    )
    btn.pack(side="left", padx=4, pady=4)
    nav_buttons[name] = btn

play_btn_mini = ctk.CTkButton(
    nav_inner,
    text="▶",
    width=32,
    height=30,
    font=("Segoe UI", 13, "bold"),
    fg_color="#2E7D32",
    hover_color="#1B5E20",
    text_color="#FFFFFF",
    corner_radius=6,
    command=play_game
)
play_btn_mini.pack(side="left", padx=(10, 2), pady=4)
CustomTooltip(play_btn_mini, "Launch Game File")

restart_btn_mini = ctk.CTkButton(
    nav_inner,
    text="🔄",
    width=32,
    height=30,
    font=("Segoe UI", 13, "bold"),
    fg_color="#C62828",
    hover_color="#B71C1C",
    text_color="#FFFFFF",
    corner_radius=6,
    command=restart_game
)
restart_btn_mini.pack(side="left", padx=2, pady=4)
CustomTooltip(restart_btn_mini, "Restart Game Process")

def open_custom_text_editor():
    editor = ctk.CTkToplevel(app)
    editor.title("Custom Config Editor")
    editor.geometry("560x520")
    editor.resizable(False, False)
    editor.attributes("-topmost", True)
    editor.grab_set()
    apply_cat_icon(editor)

    text_area = ctk.CTkTextbox(editor, font=("Consolas", 13), fg_color="#141414", text_color="#FFFFFF", border_color="#333333", border_width=1, corner_radius=8)
    text_area.pack(fill="both", expand=True, padx=15, pady=(15, 10))

    if os.path.exists(CONFIG_PATH):
        try:
            with open(CONFIG_PATH, "r", encoding="utf-8") as f:
                content = f.read()
            text_area.insert("1.0", content)
        except Exception:
            pass

    def highlight_syntax(event=None):
        text_area.tag_remove("green_val", "1.0", "end")
        text_area.tag_remove("red_val", "1.0", "end")
        
        try:
            full_text = text_area.get("1.0", "end-1c")
            lines = full_text.split("\n")
            for idx, line in enumerate(lines, start=1):
                if "=" in line and not line.strip().startswith("["):
                    parts = line.split("=", 1)
                    val_part = parts[1].strip()
                    if val_part == "1":
                        start_idx = f"{idx}.{line.find('1')}"
                        end_idx = f"{start_idx}+1c"
                        text_area.tag_add("green_val", start_idx, end_idx)
                    elif val_part == "0":
                        start_idx = f"{idx}.{line.find('0')}"
                        end_idx = f"{start_idx}+1c"
                        text_area.tag_add("red_val", start_idx, end_idx)
        except Exception:
            pass

    text_area.tag_config("green_val", foreground="#4CAF55")
    text_area.tag_config("red_val", foreground="#E53935")
    text_area.bind("<<Modified>>", lambda e: (highlight_syntax(), text_area.edit_modified(False)))
    highlight_syntax()

    bottom_bar = ctk.CTkFrame(editor, fg_color="transparent")
    bottom_bar.pack(fill="x", padx=15, pady=(0, 15))

    def save_manual_edit():
        try:
            new_content = text_area.get("1.0", "end-1c")
            os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
            with open(CONFIG_PATH, "w", encoding="utf-8") as f:
                f.write(new_content)
            global options_data
            options_data = read_options()
            editor.destroy()
        except Exception:
            pass

    btn_save = ctk.CTkButton(
        bottom_bar,
        text="💾 Save",
        font=("Segoe UI", 12, "bold"),
        fg_color="#2E7D32",
        hover_color="#1B5E20",
        height=36,
        command=save_manual_edit
    )
    btn_save.pack(fill="x")

def open_path_settings_modal():
    modal = ctk.CTkToplevel(app)
    modal.title("Meow Config")
    modal.geometry("440x360")
    modal.resizable(False, False)
    modal.attributes("-topmost", True)
    modal.grab_set()
    apply_cat_icon(modal)

    modal_icon_img = load_remote_image(URL_MAIN_ICON, "modal_main_icon.jpg", size=(36, 36))
    
    header = ctk.CTkFrame(modal, fg_color="transparent")
    header.pack(fill="x", padx=20, pady=(15, 5))

    if modal_icon_img:
        icon_lbl = ctk.CTkLabel(header, image=modal_icon_img, text="")
        icon_lbl.pack(side="left", padx=(0, 10))

    def extract_file_icon(file_path, cache_key, size=(18, 18)):
        cache_name = f"extracted_{cache_key}.png"
        cache_path = os.path.join(TEMP_DIR, cache_name)
        try:
            if not os.path.exists(file_path):
                return None
            import win32gui
            import win32ui
            import win32con
            import win32api

            large, small = win32gui.ExtractIconEx(file_path, 0)
            if small:
                for h in large:
                    win32gui.DestroyIcon(h)
                hicon = small[0]
            elif large:
                hicon = large[0]
            else:
                return None

            hdc = win32ui.CreateDCFromHandle(win32gui.GetDC(0))
            hbmp = win32ui.CreateBitmap()
            hbmp.CreateCompatibleBitmap(hdc, 32, 32)
            hdc_mem = hdc.CreateCompatibleDC()
            hdc_mem.SelectObject(hbmp)
            win32gui.DrawIconEx(hdc_mem.GetHandleAttrib(), 0, 0, hicon, 32, 32, 0, None, win32con.DI_NORMAL)

            bmp_info = hbmp.GetInfo()
            bmp_bits = hbmp.GetBitmapBits(True)
            img = Image.frombuffer(
                "RGBA",
                (bmp_info["bmWidth"], bmp_info["bmHeight"]),
                bmp_bits, "raw", "BGRA", 0, 1
            )
            img.save(cache_path)

            win32gui.DestroyIcon(hicon)
            return ctk.CTkImage(light_image=img, dark_image=img, size=size)
        except Exception:
            return None

    ini_icon = extract_file_icon(CONFIG_PATH, "ini_icon", size=(18, 18))
    exe_icon = extract_file_icon(GAME_PATH, "exe_icon", size=(18, 18))

    if ini_icon:
        path_icon_lbl = ctk.CTkLabel(header, image=ini_icon, text="")
        path_icon_lbl.pack(side="left", padx=(0, 6))

    path_display_var = ctk.StringVar(value=CONFIG_PATH)
    path_lbl = ctk.CTkLabel(header, textvariable=path_display_var, font=("Segoe UI", 10), text_color="#AAAAAA", wraplength=330, justify="left")
    path_lbl.pack(side="left", fill="x", expand=True)

    header_game = ctk.CTkFrame(modal, fg_color="transparent")
    header_game.pack(fill="x", padx=20, pady=(0, 10))

    if exe_icon:
        game_icon_lbl = ctk.CTkLabel(header_game, image=exe_icon, text="")
        game_icon_lbl.pack(side="left", padx=(0, 6))

    game_display_var = ctk.StringVar(value=GAME_PATH)
    game_lbl = ctk.CTkLabel(header_game, textvariable=game_display_var, font=("Segoe UI", 10), text_color="#888888", wraplength=360, justify="left")
    game_lbl.pack(side="left", fill="x", expand=True)

    btns_frame = ctk.CTkFrame(modal, fg_color="transparent")
    btns_frame.pack(fill="x", padx=20, pady=5)

    def change_path():
        global CONFIG_PATH
        f = filedialog.askopenfilename(title="Select options.ini", filetypes=[("INI files", "*.ini"), ("All files", "*.*")])
        if f and os.path.exists(f):
            CONFIG_PATH = f
            path_display_var.set(CONFIG_PATH)
            global options_data
            options_data = read_options()

    btn_change = ctk.CTkButton(
        btns_frame,
        text="Change options.ini Path",
        font=("Segoe UI", 11, "bold"),
        fg_color="#2B2B2B",
        hover_color="#3A3A3A",
        height=32,
        command=change_path
    )
    btn_change.pack(fill="x", pady=3)

    def change_game_path():
        global GAME_PATH
        f = filedialog.askopenfilename(title="Select isaac-ng.exe", filetypes=[("Executable", "*.exe"), ("All files", "*.*")])
        if f and os.path.exists(f):
            GAME_PATH = f
            game_display_var.set(GAME_PATH)

    btn_change_game = ctk.CTkButton(
        btns_frame,
        text="Change Isaac.exe Path",
        font=("Segoe UI", 11, "bold"),
        fg_color="#2B2B2B",
        hover_color="#3A3A3A",
        height=32,
        command=change_game_path
    )
    btn_change_game.pack(fill="x", pady=3)

    def open_folder():
        folder = os.path.dirname(CONFIG_PATH)
        if os.path.exists(folder):
            os.startfile(folder)

    btn_folder = ctk.CTkButton(
        btns_frame,
        text="Open File Location",
        font=("Segoe UI", 11, "bold"),
        fg_color="#2B2B2B",
        hover_color="#3A3A3A",
        height=32,
        command=open_folder
    )
    btn_folder.pack(fill="x", pady=3)

    def open_file():
        open_config_file()

    btn_file = ctk.CTkButton(
        btns_frame,
        text="Open File",
        font=("Segoe UI", 11, "bold"),
        fg_color="#2B2B2B",
        hover_color="#3A3A3A",
        height=32,
        command=open_file
    )
    btn_file.pack(fill="x", pady=3)

    btn_manual_editor = ctk.CTkButton(
        btns_frame,
        text="Edit File Manually",
        font=("Segoe UI", 11, "bold"),
        fg_color="#1E88E5",
        hover_color="#1565C0",
        height=32,
        command=open_custom_text_editor
    )
    btn_manual_editor.pack(fill="x", pady=3)

folder_btn_mini = ctk.CTkButton(
    nav_inner,
    text="📁",
    width=32,
    height=30,
    font=("Segoe UI", 13, "bold"),
    fg_color="#37474F",
    hover_color="#263238",
    text_color="#FFFFFF",
    corner_radius=6,
    command=open_path_settings_modal
)
folder_btn_mini.pack(side="left", padx=2, pady=4)
CustomTooltip(folder_btn_mini, "Config & Path Management")

main_center_wrapper = ctk.CTkFrame(page_main, fg_color="transparent")
main_center_wrapper.pack(expand=True)

main_card = ctk.CTkFrame(main_center_wrapper, fg_color="#1E1E1E", border_color="#2C2C2C", border_width=2, corner_radius=16, width=420, height=180)
main_card.pack(padx=20, pady=20)
main_card.pack_propagate(False)

console_val = options_data.get("EnableDebugConsole", "0") == "1"
console_var = ctk.BooleanVar(value=console_val)

card_title = ctk.CTkLabel(main_card, text="DEBUG CONSOLE", font=("Segoe UI", 16, "bold"), text_color="#888888")
card_title.pack(pady=(22, 5))

status_sub_lbl = ctk.CTkLabel(main_card, text="ENABLED" if console_val else "DISABLED", font=("Segoe UI", 12, "bold"), text_color="#4CAF50" if console_val else "#E53935")
status_sub_lbl.pack(pady=(0, 15))

def toggle_main_console():
    v = "1" if console_var.get() else "0"
    write_option("EnableDebugConsole", v)
    if console_var.get():
        status_sub_lbl.configure(text="ENABLED", text_color="#4CAF50")
    else:
        status_sub_lbl.configure(text="DISABLED", text_color="#E53935")

switch_main = ctk.CTkSwitch(
    main_card,
    text="Enable Console (~)",
    command=toggle_main_console,
    variable=console_var,
    onvalue=True,
    offvalue=False,
    font=("Segoe UI", 15, "bold"),
    switch_width=60,
    switch_height=28,
    progress_color="#43A047"
)
switch_main.pack(anchor="center")

scroll_console = ctk.CTkScrollableFrame(page_console, fg_color="#181818")
scroll_console.pack(fill="both", expand=True, padx=10, pady=5)

scroll_frame = ctk.CTkScrollableFrame(page_all, fg_color="#181818")
scroll_frame.pack(fill="both", expand=True, padx=10, pady=5)

preview_card = ctk.CTkFrame(scroll_frame, fg_color="#161616", border_color="#282828", border_width=1, corner_radius=10)

preview_title = ctk.CTkLabel(preview_card, text="MONITOR & RESOLUTION PREVIEW", font=("Segoe UI", 11, "bold"), text_color="#888888")
preview_title.pack(pady=(10, 4))

canvas = ctk.CTkCanvas(preview_card, width=320, height=160, bg="#0D0D0D", highlightthickness=0)
canvas.pack(pady=(0, 10), padx=10)

def update_preview():
    try:
        w = float(options_data.get("WindowWidth", "1917"))
        h = float(options_data.get("WindowHeight", "980"))
    except Exception:
        w, h = 1917, 980

    canvas.delete("all")
    
    max_w, max_h = 1920, 1080
    
    mon_x1, mon_y1, mon_x2, mon_y2 = 20, 15, 300, 145
    canvas.create_rectangle(mon_x1, mon_y1, mon_x2, mon_y2, outline="#333333", fill="#111111", width=2)
    
    canvas.create_text((mon_x1 + mon_x2) // 2, mon_y1 + 10, text="1920 × 1080 Monitor", fill="#555555", font=("Segoe UI", 9, "bold"))

    scale_x = (mon_x2 - mon_x1 - 24) / max_w
    scale_y = (mon_y2 - mon_y1 - 32) / max_h
    
    win_w_px = max(30, int(w * scale_x))
    win_h_px = max(20, int(h * scale_y))
    
    center_x = (mon_x1 + mon_x2) // 2
    center_y = (mon_y1 + mon_y2) // 2 + 5
    
    win_x1 = center_x - (win_w_px // 2)
    win_y1 = center_y - (win_h_px // 2)
    win_x2 = center_x + (win_w_px // 2)
    win_y2 = center_y + (win_h_px // 2)
    
    steps_x = win_w_px // 6
    steps_y = win_h_px // 6
    
    canvas.create_rectangle(win_x1, win_y1, win_x2, win_y2, outline="#338833", fill="#111B11", width=1)
    
    for i in range(1, steps_x):
        cx_line = win_x1 + i * 6
        if cx_line < win_x2:
            canvas.create_line(cx_line, win_y1, cx_line, win_y2, fill="#183618", width=1)
            
    for j in range(1, steps_y):
        cy_line = win_y1 + j * 6
        if cy_line < win_y2:
            canvas.create_line(win_x1, cy_line, win_x2, cy_line, fill="#183618", width=1)

    canvas.create_rectangle(win_x1, win_y1, win_x2, win_y2, outline="#4CAF50", fill="", width=2)
    
    canvas.create_text(center_x, center_y, text=f"{int(w)} × {int(h)}", fill="#FFFFFF", font=("Segoe UI", 9, "bold"))

widgets_ref = {}

def bind_info_tooltip(widget, key):
    desc = DESCRIPTIONS.get(key, "No description available.")
    raw_val = options_data.get(key, str(DEFAULTS[key][1]) if key in DEFAULTS else "")
    CustomTooltip(widget, lambda: f"{key}\nValue: {raw_val}\n\n{desc}")

def create_preset_buttons(parent, key, presets, slider_var, entry_var, cfg_type):
    if not presets:
        return
    presets_frame = ctk.CTkFrame(parent, fg_color="transparent")
    presets_frame.pack(fill="x", padx=10, pady=(0, 6))

    def apply_preset(val):
        slider_var.set(val)
        v_str = str(int(val)) if cfg_type in ("int", "window_dim") else f"{val:.4f}"
        entry_var.set(v_str)
        write_option(key, v_str)
        options_data[key] = v_str
        if key in ("WindowWidth", "WindowHeight"):
            update_preview()

    for label, p_val in presets:
        btn = ctk.CTkButton(
            presets_frame,
            text=f"✦ {label}",
            width=70,
            height=22,
            font=("Segoe UI", 10),
            fg_color="#2B2B2B",
            hover_color="#3A3A3A",
            command=lambda v=p_val: apply_preset(v)
        )
        btn.pack(side="left", padx=(0, 5))

def create_setting_widget(target_frame, key, info):
    cfg_type = info[0]
    raw_val = options_data.get(key, str(info[1]))

    row_frame = ctk.CTkFrame(target_frame, fg_color="#222222", corner_radius=6)
    row_frame.pack(fill="x", pady=4, padx=5)

    if cfg_type == "bool":
        val_bool = raw_val.strip() == "1"
        var = ctk.BooleanVar(value=val_bool)

        def on_switch_change():
            v = "1" if var.get() else "0"
            write_option(key, v)
            options_data[key] = v
            if key == "EnableDebugConsole":
                console_var.set(var.get())
                if var.get():
                    status_sub_lbl.configure(text="ENABLED", text_color="#4CAF50")
                else:
                    status_sub_lbl.configure(text="DISABLED", text_color="#E53935")

        sw = ctk.CTkSwitch(
            row_frame,
            text=f"⚙ {key}",
            variable=var,
            command=on_switch_change,
            onvalue=True,
            offvalue=False,
            font=("Segoe UI", 12),
            progress_color="#43A047"
        )
        sw.pack(side="left", padx=10, pady=8)
        widgets_ref[key] = var
        bind_info_tooltip(sw, key)

    elif cfg_type == "dropdown":
        top_row = ctk.CTkFrame(row_frame, fg_color="transparent")
        top_row.pack(fill="x", padx=10, pady=6)

        left_side = ctk.CTkFrame(top_row, fg_color="transparent")
        left_side.pack(side="left")

        lbl = ctk.CTkLabel(left_side, text=f"🌐 {key}", font=("Segoe UI", 12, "bold"), anchor="w")
        lbl.pack(side="left")

        if key == "Language":
            warn_lbl = ctk.CTkLabel(left_side, text=" ⚠️", font=("Segoe UI", 12), text_color="#FFC107")
            warn_lbl.pack(side="left")
            CustomTooltip(warn_lbl, "Warning: Language setting may cause unstable behavior or crashes!")

        options_list = info[2]
        current_opt = options_list[0]
        for opt in options_list:
            if opt.startswith(str(raw_val)):
                current_opt = opt
                break

        def on_select(choice):
            val_code = choice.split(" - ")[0].strip()
            write_option(key, val_code)
            options_data[key] = val_code

        combo = ctk.CTkComboBox(
            top_row,
            values=options_list,
            command=on_select,
            width=180,
            font=("Segoe UI", 11),
            fg_color="#1A1A1A",
            button_color="#2B2B2B"
        )
        combo.set(current_opt)
        combo.pack(side="right")
        widgets_ref[key] = combo
        bind_info_tooltip(lbl, key)

    elif cfg_type in ("int", "float", "window_dim"):
        min_v, max_v = info[2], info[3]
        presets = info[4] if len(info) > 4 else []
        try:
            curr_v = float(raw_val)
        except Exception:
            curr_v = float(info[1])

        top_row = ctk.CTkFrame(row_frame, fg_color="transparent")
        top_row.pack(fill="x", padx=10, pady=(6, 2))

        icon_str = "🖥 " if cfg_type == "window_dim" else "⚡ "
        lbl = ctk.CTkLabel(top_row, text=f"{icon_str}{key}", font=("Segoe UI", 12, "bold"), anchor="w")
        lbl.pack(side="left")

        entry_var = ctk.StringVar(value=str(curr_v if cfg_type == "float" else int(curr_v)))
        entry = ctk.CTkEntry(top_row, textvariable=entry_var, width=70, height=24, font=("Segoe UI", 11))
        entry.pack(side="right")

        slider_var = ctk.DoubleVar(value=curr_v)

        def on_slider(val):
            v_str = str(int(val)) if cfg_type in ("int", "window_dim") else f"{val:.4f}"
            entry_var.set(v_str)
            write_option(key, v_str)
            options_data[key] = v_str
            if cfg_type == "window_dim":
                update_preview()

        def on_entry_submit(event=None):
            try:
                val = float(entry_var.get())
                val = max(min_v, min(max_v, val))
                slider_var.set(val)
                v_str = str(int(val)) if cfg_type in ("int", "window_dim") else f"{val:.4f}"
                entry_var.set(v_str)
                write_option(key, v_str)
                options_data[key] = v_str
                if cfg_type == "window_dim":
                    update_preview()
            except Exception:
                pass

        entry.bind("<Return>", on_entry_submit)
        entry.bind("<FocusOut>", on_entry_submit)

        slider = ctk.CTkSlider(
            row_frame,
            from_=min_v,
            to=max_v,
            variable=slider_var,
            command=on_slider,
            height=16
        )
        slider.pack(fill="x", padx=10, pady=(2, 6))

        if cfg_type == "window_dim" and not presets:
            presets = [("720p", 1280 if key == "WindowWidth" else 720), 
                       ("1080p", 1920 if key == "WindowWidth" else 1080), 
                       ("1440p", 2560 if key == "WindowWidth" else 1440)]

        create_preset_buttons(row_frame, key, presets, slider_var, entry_var, cfg_type)
        widgets_ref[key] = (slider_var, entry_var)
        bind_info_tooltip(lbl, key)

for key in CONSOLE_SETTINGS:
    if key in DEFAULTS:
        create_setting_widget(scroll_console, key, DEFAULTS[key])

for key, info in DEFAULTS.items():
    create_setting_widget(scroll_frame, key, info)
    if key == "WindowHeight":
        preview_card.pack(fill="x", pady=8, padx=5)
        update_preview()

bind_fast_scroll(scroll_console)
bind_fast_scroll(scroll_frame)

def check_missing_files_and_prompt():
    global CONFIG_PATH, GAME_PATH
    has_options = os.path.exists(CONFIG_PATH)
    has_game = os.path.exists(GAME_PATH)

    if has_options and has_game:
        return

    dialog = ctk.CTkToplevel(app)
    dialog.title("Request")
    dialog.geometry("450x300")
    dialog.resizable(False, False)
    dialog.attributes("-topmost", True)
    dialog.grab_set()
    apply_cat_icon(dialog)

    title_lbl = ctk.CTkLabel(dialog, text="Request", font=("Segoe UI", 18, "bold"), text_color="#FFB300")
    title_lbl.pack(pady=(15, 5))

    desc_lbl = ctk.CTkLabel(
        dialog,
        text="Target files not found automatically.\nPlease run The Binding of Isaac or specify paths manually:",
        font=("Segoe UI", 12),
        text_color="#CCCCCC",
        justify="center"
    )
    desc_lbl.pack(pady=(0, 15))

    status_frame = ctk.CTkFrame(dialog, fg_color="#1A1A1A", corner_radius=8)
    status_frame.pack(fill="x", padx=20, pady=5)

    lbl_1 = ctk.CTkLabel(
        status_frame,
        text=f"1. Options.ini: {'✓ Found' if has_options else '✗ Missing'}",
        font=("Segoe UI", 12, "bold"),
        text_color="#4CAF50" if has_options else "#E53935",
        anchor="w"
    )
    lbl_1.pack(fill="x", padx=12, pady=6)

    lbl_2 = ctk.CTkLabel(
        status_frame,
        text=f"2. Run Isaac or select path: {'✓ Found' if has_game else '✗ Missing'}",
        font=("Segoe UI", 12, "bold"),
        text_color="#4CAF50" if has_game else "#E53935",
        anchor="w"
    )
    lbl_2.pack(fill="x", padx=12, pady=(0, 6))

    def auto_scan_from_process():
        nonlocal has_options, has_game
        global CONFIG_PATH, GAME_PATH
        found = False
        for proc in psutil.process_iter(['name', 'exe']):
            try:
                if proc.info['name'] and proc.info['name'].lower() == "isaac-ng.exe":
                    exe_p = proc.info['exe']
                    if exe_p and os.path.exists(exe_p):
                        GAME_PATH = exe_p
                        has_game = True
                        found = True
                        lbl_2.configure(text="2. Run Isaac or select path: ✓ Found (Process)", text_color="#4CAF50")
            except Exception:
                pass
        
        opt = auto_detect_options_ini()
        if opt:
            CONFIG_PATH = opt
            has_options = True
            lbl_1.configure(text="1. Options.ini: ✓ Found", text_color="#4CAF50")

        if has_options and has_game:
            dialog.after(800, dialog.destroy)

    def select_exe_file():
        global GAME_PATH
        nonlocal has_game
        f = filedialog.askopenfilename(title="Select isaac-ng.exe", filetypes=[("Executable", "*.exe")])
        if f and os.path.exists(f):
            GAME_PATH = f
            has_game = True
            lbl_2.configure(text="2. Run Isaac or select path: ✓ Selected", text_color="#4CAF50")
            if has_options and has_game:
                dialog.after(800, dialog.destroy)

    def select_ini_file():
        global CONFIG_PATH
        nonlocal has_options
        f = filedialog.askopenfilename(title="Select options.ini", filetypes=[("INI files", "*.ini")])
        if f and os.path.exists(f):
            CONFIG_PATH = f
            has_options = True
            lbl_1.configure(text="1. Options.ini: ✓ Selected", text_color="#4CAF50")
            if has_options and has_game:
                dialog.after(800, dialog.destroy)

    btn_frame = ctk.CTkFrame(dialog, fg_color="transparent")
    btn_frame.pack(fill="x", padx=20, pady=15)

    scan_btn = ctk.CTkButton(
        btn_frame,
        text="🔍 Find Running Process",
        font=("Segoe UI", 11, "bold"),
        fg_color="#1E88E5",
        hover_color="#1565C0",
        command=auto_scan_from_process
    )
    scan_btn.pack(side="top", fill="x", pady=3)

    sub_btns = ctk.CTkFrame(btn_frame, fg_color="transparent")
    sub_btns.pack(fill="x", pady=3)

    path_game_btn = ctk.CTkButton(
        sub_btns,
        text="Browse Game .exe",
        font=("Segoe UI", 10),
        fg_color="#2B2B2B",
        hover_color="#3A3A3A",
        width=190,
        command=select_exe_file
    )
    path_game_btn.pack(side="left", padx=(0, 5))

    path_ini_btn = ctk.CTkButton(
        sub_btns,
        text="Browse options.ini",
        font=("Segoe UI", 10),
        fg_color="#2B2B2B",
        hover_color="#3A3A3A",
        width=190,
        command=select_ini_file
    )
    path_ini_btn.pack(side="right")

show_page("Main")
update_game_status_indicator()
app.after(500, check_missing_files_and_prompt)

app.mainloop()