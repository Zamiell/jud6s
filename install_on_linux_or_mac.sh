#!/bin/sh

# This is the variable to set if you want to use another directory than the
# default one !
user_defined_resources_path=""


# Don't edit below this please ;)

detected_path=""
user_choice=""

autodetect_resources() {
    # Attempt to autodetect the resource folder if the user didn't specify one
    if [ ! -z "$user_defined_resources_path" ]; then
        echo "Using user-defined path to resources."
        detected_path=$user_defined_resources_path
        return
    fi
    user_os=`uname` 
    steam_root=""
    case "$user_os" in 
        linux|Linux)
            echo "Linux has been detected, if this is wrong please exit the script"
            steam_root="$HOME/.local/share/Steam"
            ;;
        Darwin*|darwin*)
            echo "Mac OS has been detected, if this is wrong please exit the script"
            steam_root="$HOME/Library/Application Support/Steam"
            ;;
        *)
            echo "ERROR: Failed to detect OS, (uname returned \"$user_os\")"
            echo "This script is intended to be ran on Linux or Mac OS,"
            echo "If you are indeed on one of these platforms, please create a bug report with this message."
            exit 1
            ;;
    esac
    detected_path="$steam_root/steamapps/common/The Binding of Isaac Rebirth/resources"
}

get_user_choice() {
    echo "^+-------------------------------------------------------------^+"
    echo "^| WARNING: This script will delete all of the current mods    ^|"
    echo "^|          in your Afterbirth resources folder. If this is    ^|"
    echo "^|          is not what you want, exit this script now.        ^|"
    echo "^+-------------------------------------------------------------^+"
    echo ""
    echo "Choose a ruleset:"
    echo "  1: Normal"
    echo "  2: More Options"
    echo "  3: Seeded"
    echo "  4: Dark Room"
    echo "  5: Seeded Dark Room"
    echo ""
    echo "Or:"
    echo "  6: Uninstall all mods"
    echo "  0 or nothing: exit the script"
    echo ""
    done=false
    while [ "$done" = false ];
    do
        echo "Type your choice and hit enter :"
        read choice
        if [ ! -z ${choice} ]; then
            case "$choice" in
                0|1|2|3|4|5|6)
                    user_choice=$choice
                    done=true
                    ;;
                *)
                    echo "ERROR: Wrong choice, please choose again."
                    ;;
            esac
        else
            echo "Nothing selected"
            # 0 means exit
            user_choice="0"
            done=true
        fi
    done
    echo ""
}

cd_and_check_directory() {
    # cd and Check for packed directory to be sure we are not in some random
    # directory deleting other random files...
    cd "$detected_path"
    if [ "$?" -ne "0" ]; then
        echo "ERROR: Couldn't cd to resources directory, exiting"
        exit 1
    fi
    if [ ! -d "packed" ]; then
        echo "ERROR: Resources directory has no packed directory, aborting."
        echo "Please check the detected path !"
        exit 1
    fi
}

remove_all_mods() {
    cd_and_check_directory
    echo "Listing all files but packed :"
    filelist=`find . ! \( -wholename './packed*' -o -name '.' \)`
    if [ ! -z "$filelist" ]; then
        # If we'd just echo filelist it would be awfully displayed
        find . ! \( -wholename './packed*' -o -name '.' \)
        echo "All the above things will be removed, proceed ? (y/N)"
        # One more confirmation because we don't want to screw up
        read confirm
        if [ -z "$confirm" -o "$confirm" != "y" ]; then
            echo "Exiting without removing"
            exit 0
        else
            echo "Removing things."
            find . ! \( -wholename './packed*' -o -name '.' \) -exec rm -rf {} +
        fi
    else
        echo "No file to remove, continue"
    fi
}

# Warning, this function does no check at all, please ensure input are validated
# before executing it.
# First parameter should be a ruleset ID
install_ruleset() {
    echo "Removing all mods before installing"
    here=`pwd`
    remove_all_mods
    cd $here
    echo "Installing ruleset $1"
    echo "Executing : cp -r Ruleset\ $1*/* \"$detected_path\""
    cp -r Ruleset\ $1*/* "$detected_path"
}


autodetect_resources

echo "Selected path is  \"$detected_path\"\n"

# Check the detected path
if [ ! -d "$detected_path" ]; then
    echo "ERROR: The detected path to resources folder is not a directory."
    echo "If your steam installation directory is not standard,"
    echo "please edit this file to provide the path to your resources directory."
    exit 1
fi

get_user_choice

if [ "$user_choice" -eq "0" ]; then
    echo "Doing nothing and exiting."
    exit 0
elif [ "$user_choice" -eq "6" ]; then
    remove_all_mods
    echo "Done, exiting"
    exit 0
else
    # get_user_choice has validated the input
    install_ruleset "$user_choice"
    if [ "$?" -eq "0" ]; then
        echo "Ruleset successfully installed, exiting"
        exit 0
    else
        echo "An error has occured during the installation,"
        echo "please retry or fill a bug report"
        exit 1
    fi
fi
