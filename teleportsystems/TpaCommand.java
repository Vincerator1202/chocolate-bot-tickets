package de.dev_MisterMo2022.farmwelt.Farmwelt.teleportsystems;

import org.bukkit.Bukkit;
import org.bukkit.command.*;
import org.bukkit.entity.Player;

public class TpaCommand implements CommandExecutor {

    @Override
    public boolean onCommand(CommandSender sender, Command cmd, String label, String[] args) {

        if (!(sender instanceof Player)) return true;
        Player player = (Player) sender;

        if (args.length != 1) {
            player.sendMessage("§cUsage: /tpa <player>");
            return true;
        }

        Player target = Bukkit.getPlayer(args[0]);
        if (target == null) {
            player.sendMessage("§cPlayer not found.");
            return true;
        }

        FarmweltCore.instance.tpaRequests.put(target.getUniqueId(), player.getUniqueId());

        target.sendMessage("§e" + player.getName() + " wants to teleport to you.");
        target.sendMessage("§aType /tpaccept to accept.");

        player.sendMessage("§aTeleport request sent.");
        return true;
    }
}