package de.dev_MisterMo2022.farmwelt.Farmwelt.teleportsystems;

import org.bukkit.command.*;
import org.bukkit.entity.Player;

public class SetSpawnCommand implements CommandExecutor {

    @Override
    public boolean onCommand(CommandSender sender, Command cmd, String label, String[] args) {

        if (!(sender instanceof Player)) return true;
        Player player = (Player) sender;

        FarmweltCore.instance.getConfig().set("spawn", player.getLocation());
        FarmweltCore.instance.saveConfig();

        player.sendMessage("§aSpawn set!");
        return true;
    }
}