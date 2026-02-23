package de.dev_MisterMo2022.farmwelt.Farmwelt.teleportsystems;

import org.bukkit.Bukkit;
import org.bukkit.plugin.java.JavaPlugin;

import java.io.File;
import java.util.HashMap;
import java.util.UUID;

public class FarmweltCore extends JavaPlugin {

    public static FarmweltCore instance;
    public HashMap<UUID, UUID> tpaRequests = new HashMap<>();

    @Override
    public void onEnable() {
        instance = this;

        saveDefaultConfig();

        getCommand("tpa").setExecutor(new TpaCommand());
        getCommand("tpaccept").setExecutor(new TpAcceptCommand());
        getCommand("spawn").setExecutor(new SpawnCommand());
        getCommand("setspawn").setExecutor(new SetSpawnCommand());
        getCommand("backup").setExecutor(new BackupCommand());

        getLogger().info("Farmwelt TeleportSystem enabled!");
    }
}