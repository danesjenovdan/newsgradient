# Development Environment Setup for Android on Debian/Ubuntu/WSL

## 1. Prerequisites

### Node 16

```bash
nvm install 16

# nvm use 16
node -v # `v16.5.0` or similar
```

### Java 14

```bash
sudo apt install openjdk-14-jdk

# sudo update-java-alternatives -s java-1.14.0-openjdk-amd64
java --version # `openjdk 14.0.2` or similar
javac --version # `javac 14.0.2` or similar
```

### Android Studio

```bash
# download
wget https://redirector.gvt1.com/edgedl/android/studio/ide-zips/4.2.2.0/android-studio-ide-202.7486908-linux.tar.gz
# extract
tar -xzf android-studio-ide-202.7486908-linux.tar.gz
# run
cd android-studio/bin
./studio.sh
```

Install required SDK packages:
- Finish the first time setup (install SDK to `~/android-sdk` when asked)
- On the welcome screen click "Configure" > "Android SDK"
- Under "SDK Platforms":
  - Select "Android 11" (API Level 30)
- Under "SDK Tools"
  - Select "Show Package Details" (bottom right)
  - Select "Android SDK Build-Tools 30.0.3"
  - Select "Android SDK Command-line Tools (latest)"
- Click OK and finish the installation
- Close the welcome screen

Setup environment:

- Add environment variables to .bashrc

```bash
export ANDROID_HOME="$HOME/android-sdk" # change if installed elsewhere
export PATH="$PATH:$ANDROID_HOME/platform-tools"
```

- Source .bashrc (or restart terminal)

```bash
source ~/.bashrc
```

---

## 2. Development setup

### Install dependencies

```bash
npm install
```

### Check environment

```bash
npm run check
```

### Check connected devices

- Connect your phone via USB and make sure USB debugging is enabled on it
- You may need to change USB mode to "File Transfer" on some devices
- Run the following command to list all connected devices:

```bash
npx ns device
```

### Remote debugging via WiFi (optional)

- Make sure your phone is detected via USB (previous step)
- Restart adbd for listening on TCP:

```bash
adb tcpip 5555
```

- Make sure your computer and phone are on the same local network
- Find out the local IP of your phone (WiFi settings > Network details > Advanced > IP address)
- Connect to your phone with adb:

```bash
adb connect 192.168.1.123 # change to your phone's IP
```

- Run the following command to list all connected devices:

```bash
npx ns device
```

  - `Device Identifier` should be `IP:PORT`
  - `Connection Type` may still say `USB` (this is fine)

---

## 3. Run app on connected device for development

```bash
npm run dev
```
