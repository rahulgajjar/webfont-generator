import subprocess
import os

def cleanup(srcpath, destpath):
    for root, subFolders, files in os.walk(srcpath):
        for file in files:
            if file.lower().endswith((".ttf", ".otf")):
                font_path = os.path.join(root, file)
                
                # Rename 'OTF' to 'Static' and 'TTF' to 'Variable'
                relative_path = os.path.relpath(font_path, srcpath)
                relative_dir = os.path.dirname(relative_path)
                
                if 'OTF' in relative_dir:
                    relative_dir = relative_dir.replace('OTF', 'Static')
                elif 'TTF' in relative_dir:
                    relative_dir = relative_dir.replace('TTF', 'Variable')
                
                output_dir = os.path.join(destpath, relative_dir)
                
                os.makedirs(output_dir, exist_ok=True)

                args = ["./bin/generate-webfonts", font_path, "-o", output_dir, "-f", "woff2,otf"]
                subprocess.call(args)

    print("Generated Webfonts")

def main():
    srcpath = "fonts"
    destpath = "output"
    cleanup(srcpath, destpath)

if __name__ == '__main__':
    main()
