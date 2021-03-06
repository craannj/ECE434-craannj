#include <linux/build-salt.h>
#include <linux/module.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

BUILD_SALT;

MODULE_INFO(vermagic, VERMAGIC_STRING);
MODULE_INFO(name, KBUILD_MODNAME);

__visible struct module __this_module
__attribute__((section(".gnu.linkonce.this_module"))) = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};

#ifdef CONFIG_RETPOLINE
MODULE_INFO(retpoline, "Y");
#endif

static const struct modversion_info ____versions[]
__used
__attribute__((section("__versions"))) = {
	{ 0x1563ff79, "module_layout" },
	{ 0x3a043d7e, "class_unregister" },
	{ 0x1ddbd245, "device_destroy" },
	{ 0xc71e5d08, "class_destroy" },
	{ 0xe9958090, "device_create" },
	{ 0x6bc3fbc0, "__unregister_chrdev" },
	{ 0x46508d2, "__class_create" },
	{ 0xc25dd626, "__register_chrdev" },
	{ 0xf4fa543b, "arm_copy_to_user" },
	{ 0x1e047854, "warn_slowpath_fmt" },
	{ 0x5f754e5a, "memset" },
	{ 0x28cc25db, "arm_copy_from_user" },
	{ 0x88db9f48, "__check_object_size" },
	{ 0x2e5810c6, "__aeabi_unwind_cpp_pr1" },
	{ 0x7c32d0f0, "printk" },
	{ 0xb1ad28e0, "__gnu_mcount_nc" },
};

static const char __module_depends[]
__used
__attribute__((section(".modinfo"))) =
"depends=";


MODULE_INFO(srcversion, "F04127A55074B981D316F53");
