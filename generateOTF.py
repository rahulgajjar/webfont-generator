import subprocess, os, shutil, stat, platform, json
def cleanup():
    srcpath = "fonts"
    destpath = "output"

    for root, subFolders, files in os.walk(srcpath):
        for file in files:
            if (".ttf" in file) or (".otf" in file):
                full_path = os.path.join(srcpath,file)
                args = ["./bin/generate-webfonts"]
                args.extend([full_path])
                args.extend(["-o"])
                args.extend([destpath])

                subprocess.call(args)
            continue
        break
    # for rooot, subFoolders, filess in os.walk(destpath):
    #     for file in filess:
    #         if ".eot" in file:
    #             os.remove(os.path.join(destpath, file))
    #         if ".svg" in file:
    #             os.remove(os.path.join(destpath, file))
    #         continue
    #     break

    print("Generated Webfonts")

def main():
    cleanup()

if __name__ == '__main__':
    main()