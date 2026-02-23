package de.dev_MisterMo2022.farmwelt.Farmwelt.teleportsystems;

import org.bukkit.Bukkit;
import org.bukkit.command.*;

import java.io.File;

public class BackupCommand implements CommandExecutor {

    @Override
    public boolean onCommand(CommandSender sender, Command cmd, String label, String[] args) {

        File worldFolder = new File(Bukkit.getWorldContainer(), "world");
        File backupFolder = new File("plugins/FarmweltCore/backups");

        if (!backupFolder.exists()) backupFolder.mkdirs();

        File dest = new File(backupFolder, "backup-" + System.currentTimeMillis());
        worldFolder.renameTo(dest);

        sender.sendMessage("§aBackup created.");
        return true;
    }
}