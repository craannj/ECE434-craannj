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
	{ 0xec139859, "param_ops_uint" },
	{ 0xfe990052, "gpio_free" },
	{ 0xbac4863f, "gpiod_unexport" },
	{ 0xb33fefdf, "kthread_stop" },
	{ 0xc126202b, "wake_up_process" },
	{ 0x4cdb6d62, "kthread_create_on_node" },
	{ 0x3df62084, "gpiod_export" },
	{ 0xabea3285, "gpiod_direction_output_raw" },
	{ 0x47229b5c, "gpio_request" },
	{ 0xf4ef9a03, "kobject_put" },
	{ 0xf1fa3b08, "sysfs_create_group" },
	{ 0x2a255cef, "kobject_create_and_add" },
	{ 0x93c630bd, "kernel_kobj" },
	{ 0x20c55ae0, "sscanf" },
	{ 0x84b183ae, "strncmp" },
	{ 0xdb7305a1, "__stack_chk_fail" },
	{ 0xf9a482f9, "msleep" },
	{ 0xf1c6a65, "gpiod_set_raw_value" },
	{ 0x7a974ba7, "gpio_to_desc" },
	{ 0xb3f7646e, "kthread_should_stop" },
	{ 0x7c32d0f0, "printk" },
	{ 0x8f678b07, "__stack_chk_guard" },
	{ 0x2e5810c6, "__aeabi_unwind_cpp_pr1" },
	{ 0x91715312, "sprintf" },
	{ 0xb1ad28e0, "__gnu_mcount_nc" },
};

static const char __module_depends[]
__used
__attribute__((section(".modinfo"))) =
"depends=";


MODULE_INFO(srcversion, "B2CD6BA092513447B6DBA55");
