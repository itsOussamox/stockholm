import os

# The folder stockholm is allowed to work in — nothing outside this
INFECTION_DIR = os.path.join(os.path.expanduser("~"), "infection")

# File extensions targeted by WannaCry
WANNACRY_EXTENSIONS = {
    ".der", ".pfx", ".key", ".crt", ".csr", ".p12", ".pem",
    ".odt", ".ott", ".sxw", ".stw", ".uot", ".doc", ".docx",
    ".docb", ".docm", ".dot", ".dotm", ".dotx", ".wps", ".wpt",
    ".xls", ".xlsx", ".xlsm", ".xlsb", ".xlw", ".xlt", ".xlm",
    ".xlc", ".xltx", ".xltm", ".xlsb", ".wk1", ".wb2", ".wq1",
    ".ods", ".ots", ".sxc", ".stc", ".dif", ".slk", ".ppt",
    ".pptx", ".pptm", ".pot", ".pps", ".ppsm", ".ppsx", ".ppam",
    ".potx", ".potm", ".edb", ".hwp", ".602", ".sxi", ".sti",
    ".sldx", ".sldm", ".vdi", ".vmdk", ".vmx", ".gpg", ".aes",
    ".arc", ".asc", ".bck", ".bkp", ".bak", ".vsd", ".vsdx",
    ".txt", ".csv", ".rtf", ".123", ".wks", ".pdf", ".dwg",
    ".onetoc2", ".snt", ".jpg", ".jpeg", ".png", ".gif", ".bmp",
    ".raw", ".tif", ".tiff", ".nef", ".psd", ".svg", ".ai",
    ".mp3", ".mp4", ".wma", ".wmv", ".avi", ".mov", ".flv",
    ".mkv", ".mpeg", ".mpg", ".m4u", ".m3u", ".mid", ".wav",
    ".3g2", ".3gp", ".asf", ".iso", ".zip", ".rar", ".7z",
    ".gz", ".tar", ".tgz", ".bz2", ".PAQ", ".tbk", ".backup",
    ".sql", ".mdb", ".accdb", ".db", ".dbf", ".odb", ".frm",
    ".myd", ".myi", ".ibd", ".mdf", ".ldf", ".sqlite3", ".sqlitedb",
    ".java", ".class", ".jar", ".jsp", ".php", ".asp", ".js",
    ".vb", ".vbs", ".ps1", ".bat", ".cmd", ".asm", ".h",
    ".pas", ".cpp", ".c", ".cs", ".suo", ".sln", ".brd",
    ".sch", ".dch", ".dip", ".djvu", ".fla", ".swf", ".cgm",
}


def get_infection_dir():
    """
    Returns the path to ~/infection if it exists.
    Exits cleanly if it doesn't — we never create it ourselves.
    """
    if not os.path.isdir(INFECTION_DIR):
        raise FileNotFoundError(
            f"[!] Folder not found: {INFECTION_DIR}\n"
            f"    Create it and add some files before running stockholm."
        )
    return INFECTION_DIR


def get_target_files(folder):
    """
    Walk through the infection folder and return all files
    whose extension is in the WannaCry list.
    Already-encrypted .ft files are skipped.
    """
    targets = []

    for root, _, files in os.walk(folder):
        for filename in files:
            name, ext = os.path.splitext(filename)
            if ext == ".ft":
                continue
            if ext.lower() in WANNACRY_EXTENSIONS:
                targets.append(os.path.join(root, filename))

    return targets


def get_encrypted_files(folder):
    """
    Walk through the infection folder and return all .ft files
    (used when reversing the infection).
    """
    encrypted = []

    for root, _, files in os.walk(folder):
        for filename in files:
            if filename.endswith(".ft"):
                encrypted.append(os.path.join(root, filename))

    return encrypted