from collections import OrderedDict
from collections.abc import Callable, Iterator, Mapping, Sequence
from typing import Any, Generic, Iterable, TypeVar
from typing_extensions import Literal, TypedDict

from django.contrib.admin.filters import ListFilter
from django.contrib.admin.helpers import ActionForm
from django.contrib.admin.models import LogEntry
from django.contrib.admin.sites import AdminSite
from django.contrib.admin.views.main import ChangeList
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.contrib.contenttypes.models import ContentType
from django.core.checks.messages import CheckMessage
from django.core.paginator import Paginator
from django.db.models.base import Model
from django.db.models.fields import Field
from django.db.models.fields.related import ForeignKey, ManyToManyField, RelatedField
from django.db.models.options import Options
from django.db.models.query import QuerySet
from django.forms.fields import TypedChoiceField
from django.forms.forms import BaseForm
from django.forms.models import (
    BaseInlineFormSet,
    BaseModelFormSet,
    ModelChoiceField,
    ModelForm,
    ModelMultipleChoiceField,
)
from django.forms.widgets import Media
from django.http.request import HttpRequest
from django.http.response import (
    HttpResponse,
    HttpResponseBase,
    HttpResponseRedirect,
    JsonResponse,
)
from django.template.response import TemplateResponse
from django.urls.resolvers import URLPattern
from django.utils.safestring import SafeText

IS_POPUP_VAR: str
TO_FIELD_VAR: str
HORIZONTAL: Literal[1] = ...
VERTICAL: Literal[2] = ...

_Direction = Literal[1, 2]

def get_content_type_for_model(obj: type[Model] | Model) -> ContentType: ...
def get_ul_class(radio_style: int) -> str: ...

class IncorrectLookupParameters(Exception): ...

FORMFIELD_FOR_DBFIELD_DEFAULTS: Any
csrf_protect_m: Any

class _OptionalFieldOpts(TypedDict, total=False):
    classes: Sequence[str]
    description: str

class _FieldOpts(_OptionalFieldOpts, total=True):
    fields: Sequence[str | Sequence[str]]

# Workaround for mypy issue, a Sequence type should be preferred here.
# https://github.com/python/mypy/issues/8921
# _FieldsetSpec = Sequence[tuple[str | None, _FieldOpts]]
_T = TypeVar("_T")
_ListOrTuple = tuple[_T, ...] | list[_T]
_FieldsetSpec = _ListOrTuple[tuple[str | None, _FieldOpts]]

# Generic type specifically for models, for use in BaseModelAdmin and subclasses
# https://github.com/typeddjango/django-stubs/issues/482
_ModelT = TypeVar("_ModelT", bound=Model)

class BaseModelAdmin(Generic[_ModelT]):
    autocomplete_fields: Sequence[str] = ...
    raw_id_fields: Sequence[str] = ...
    fields: Sequence[str | Sequence[str]] = ...
    exclude: Sequence[str] = ...
    fieldsets: _FieldsetSpec = ...
    form: type[BaseForm] = ...
    filter_vertical: Sequence[str] = ...
    filter_horizontal: Sequence[str] = ...
    radio_fields: Mapping[str, _Direction] = ...
    prepopulated_fields: Mapping[str, Sequence[str]] = ...
    formfield_overrides: Mapping[type[Field[Any, Any]], Mapping[str, Any]] = ...
    readonly_fields: Sequence[str | Callable[[_ModelT], Any]] = ...
    ordering: Sequence[str] | None = ...
    sortable_by: Sequence[str] | None = ...
    view_on_site: bool = ...
    show_full_result_count: bool = ...
    checks_class: Any = ...
    def check(self, **kwargs: Any) -> list[CheckMessage]: ...
    def formfield_for_dbfield(
        self, db_field: Field[Any, Any], request: HttpRequest | None, **kwargs: Any
    ) -> Field[Any, Any] | None: ...
    def formfield_for_choice_field(
        self, db_field: Field[Any, Any], request: HttpRequest | None, **kwargs: Any
    ) -> TypedChoiceField: ...
    def get_field_queryset(
        self, db: None, db_field: RelatedField[Any, Any], request: HttpRequest | None
    ) -> QuerySet[Any] | None: ...
    def formfield_for_foreignkey(
        self, db_field: ForeignKey[Any], request: HttpRequest | None, **kwargs: Any
    ) -> ModelChoiceField | None: ...
    def formfield_for_manytomany(
        self,
        db_field: ManyToManyField[Any, Any],
        request: HttpRequest | None,
        **kwargs: Any
    ) -> ModelMultipleChoiceField: ...
    def get_autocomplete_fields(self, request: HttpRequest) -> Sequence[str]: ...
    def get_view_on_site_url(self, obj: _ModelT | None = ...) -> str | None: ...
    def get_empty_value_display(self) -> SafeText: ...
    def get_exclude(
        self, request: HttpRequest, obj: _ModelT | None = ...
    ) -> Sequence[str]: ...
    def get_fields(
        self, request: HttpRequest, obj: _ModelT | None = ...
    ) -> Sequence[Callable[..., Any] | str]: ...
    def get_fieldsets(
        self, request: HttpRequest, obj: _ModelT | None = ...
    ) -> list[tuple[str | None, dict[str, Any]]]: ...
    def get_ordering(self, request: HttpRequest) -> list[str] | tuple[Any, ...]: ...
    def get_readonly_fields(
        self, request: HttpRequest, obj: _ModelT | None = ...
    ) -> list[str] | tuple[Any, ...]: ...
    def get_prepopulated_fields(
        self, request: HttpRequest, obj: _ModelT | None = ...
    ) -> dict[str, tuple[str]]: ...
    def get_queryset(self, request: HttpRequest) -> QuerySet[_ModelT]: ...
    def get_sortable_by(
        self, request: HttpRequest
    ) -> list[Callable[..., Any]] | list[str] | tuple[Any, ...]: ...
    def get_inlines(
        self, request: HttpRequest, obj: _ModelT | None
    ) -> Iterable[type[InlineModelAdmin[Any]]]: ...
    def lookup_allowed(self, lookup: str, value: str) -> bool: ...
    def to_field_allowed(self, request: HttpRequest, to_field: str) -> bool: ...
    def has_add_permission(self, request: HttpRequest) -> bool: ...
    def has_change_permission(
        self, request: HttpRequest, obj: _ModelT | None = ...
    ) -> bool: ...
    def has_delete_permission(
        self, request: HttpRequest, obj: _ModelT | None = ...
    ) -> bool: ...
    def has_view_permission(
        self, request: HttpRequest, obj: _ModelT | None = ...
    ) -> bool: ...
    def has_module_permission(self, request: HttpRequest) -> bool: ...

class ModelAdmin(BaseModelAdmin[_ModelT]):
    list_display: Sequence[str | Callable[[_ModelT], Any]] = ...
    list_display_links: Sequence[str | Callable[..., Any]] | None = ...
    list_filter: Sequence[str | type[ListFilter] | tuple[str, type[ListFilter]]] = ...
    list_select_related: bool | Sequence[str] = ...
    list_per_page: int = ...
    list_max_show_all: int = ...
    list_editable: Sequence[str] = ...
    search_fields: Sequence[str] = ...
    date_hierarchy: str | None = ...
    save_as: bool = ...
    save_as_continue: bool = ...
    save_on_top: bool = ...
    paginator: type[Any] = ...
    preserve_filters: bool = ...
    inlines: Sequence[type[InlineModelAdmin[Any]]] = ...
    add_form_template: str = ...
    change_form_template: str = ...
    change_list_template: str = ...
    delete_confirmation_template: str = ...
    delete_selected_confirmation_template: str = ...
    object_history_template: str = ...
    popup_response_template: str = ...
    actions: Sequence[
        Callable[[ModelAdmin[Any], HttpRequest, QuerySet[Any]], HttpResponse | None]
        | str
    ] | None = ...
    action_form: type[ActionForm] = ...
    actions_on_top: bool = ...
    actions_on_bottom: bool = ...
    actions_selection_counter: bool = ...
    model: type[_ModelT] = ...
    opts: Options[_ModelT] = ...
    admin_site: AdminSite = ...
    def __init__(self, model: type[_ModelT], admin_site: AdminSite | None) -> None: ...
    def get_inline_instances(
        self, request: HttpRequest, obj: _ModelT | None = ...
    ) -> list[InlineModelAdmin[Any]]: ...
    def get_urls(self) -> list[URLPattern]: ...
    @property
    def urls(self) -> list[URLPattern]: ...
    @property
    def media(self) -> Media: ...
    def get_model_perms(self, request: HttpRequest) -> dict[str, bool]: ...
    def get_form(
        self,
        request: HttpRequest,
        obj: _ModelT | None = ...,
        change: bool = ...,
        **kwargs: Any
    ) -> type[ModelForm]: ...
    def get_changelist(
        self, request: HttpRequest, **kwargs: Any
    ) -> type[ChangeList]: ...
    def get_changelist_instance(self, request: HttpRequest) -> ChangeList: ...
    def get_object(
        self, request: HttpRequest, object_id: str, from_field: None = ...
    ) -> _ModelT | None: ...
    def get_changelist_form(
        self, request: HttpRequest, **kwargs: Any
    ) -> type[ModelForm]: ...
    def get_changelist_formset(
        self, request: HttpRequest, **kwargs: Any
    ) -> type[BaseModelFormSet]: ...
    def get_formsets_with_inlines(
        self, request: HttpRequest, obj: _ModelT | None = ...
    ) -> Iterator[Any]: ...
    def get_paginator(
        self,
        request: HttpRequest,
        queryset: QuerySet[_ModelT],
        per_page: int,
        orphans: int = ...,
        allow_empty_first_page: bool = ...,
    ) -> Paginator: ...
    def log_addition(
        self, request: HttpRequest, object: _ModelT, message: Any
    ) -> LogEntry: ...
    def log_change(
        self, request: HttpRequest, object: _ModelT, message: Any
    ) -> LogEntry: ...
    def log_deletion(
        self, request: HttpRequest, object: _ModelT, object_repr: str
    ) -> LogEntry: ...
    def action_checkbox(self, obj: _ModelT) -> SafeText: ...
    def get_actions(self, request: HttpRequest) -> OrderedDict[Any, Any]: ...
    def get_action_choices(
        self, request: HttpRequest, default_choices: list[tuple[str, str]] = ...
    ) -> list[tuple[str, str]]: ...
    def get_action(
        self, action: Callable[..., Any] | str
    ) -> tuple[Callable[..., Any], str, str]: ...
    def get_list_display(self, request: HttpRequest) -> Sequence[str]: ...
    def get_list_display_links(
        self, request: HttpRequest, list_display: Sequence[str]
    ) -> Sequence[str] | None: ...
    def get_list_filter(self, request: HttpRequest) -> Sequence[str]: ...
    def get_list_select_related(self, request: HttpRequest) -> Sequence[str]: ...
    def get_search_fields(self, request: HttpRequest) -> list[str]: ...
    def get_search_results(
        self, request: HttpRequest, queryset: QuerySet[Any], search_term: str
    ) -> tuple[QuerySet[Any], bool]: ...
    def get_preserved_filters(self, request: HttpRequest) -> str: ...
    def construct_change_message(
        self,
        request: HttpRequest,
        form: AdminPasswordChangeForm,
        formsets: None,
        add: bool = ...,
    ) -> list[dict[str, dict[str, list[str]]]]: ...
    def message_user(
        self,
        request: HttpRequest,
        message: str,
        level: int | str = ...,
        extra_tags: str = ...,
        fail_silently: bool = ...,
    ) -> None: ...
    def save_form(
        self, request: HttpRequest, form: ModelForm, change: bool
    ) -> _ModelT: ...
    def save_model(
        self, request: HttpRequest, obj: _ModelT, form: ModelForm, change: bool
    ) -> None: ...
    def delete_model(self, request: HttpRequest, obj: _ModelT) -> None: ...
    def delete_queryset(
        self, request: HttpRequest, queryset: QuerySet[_ModelT]
    ) -> None: ...
    def save_formset(
        self,
        request: HttpRequest,
        form: ModelForm,
        formset: BaseModelFormSet,
        change: bool,
    ) -> None: ...
    def save_related(
        self,
        request: HttpRequest,
        form: ModelForm,
        formsets: BaseModelFormSet,
        change: bool,
    ) -> None: ...
    def render_change_form(
        self,
        request: HttpRequest,
        context: Mapping[str, Any],
        add: bool = ...,
        change: bool = ...,
        form_url: str = ...,
        obj: _ModelT | None = ...,
    ) -> TemplateResponse: ...
    def response_add(
        self, request: HttpRequest, obj: _ModelT, post_url_continue: str | None = ...
    ) -> HttpResponse: ...
    def response_change(self, request: HttpRequest, obj: _ModelT) -> HttpResponse: ...
    def response_post_save_add(
        self, request: HttpRequest, obj: _ModelT
    ) -> HttpResponseRedirect: ...
    def response_post_save_change(
        self, request: HttpRequest, obj: _ModelT
    ) -> HttpResponseRedirect: ...
    def response_action(
        self, request: HttpRequest, queryset: QuerySet[_ModelT]
    ) -> HttpResponseBase | None: ...
    def response_delete(
        self, request: HttpRequest, obj_display: str, obj_id: int
    ) -> HttpResponse: ...
    def render_delete_form(
        self, request: HttpRequest, context: Mapping[str, Any]
    ) -> TemplateResponse: ...
    def get_inline_formsets(
        self,
        request: HttpRequest,
        formsets: list[Any],
        inline_instances: list[Any],
        obj: _ModelT | None = ...,
    ) -> list[Any]: ...
    def get_changeform_initial_data(self, request: HttpRequest) -> dict[str, str]: ...
    def changeform_view(
        self,
        request: HttpRequest,
        object_id: str | None = ...,
        form_url: str = ...,
        extra_context: dict[str, bool] | None = ...,
    ) -> TemplateResponse: ...
    def autocomplete_view(self, request: HttpRequest) -> JsonResponse: ...
    def add_view(
        self, request: HttpRequest, form_url: str = ..., extra_context: None = ...
    ) -> HttpResponse: ...
    def change_view(
        self,
        request: HttpRequest,
        object_id: str,
        form_url: str = ...,
        extra_context: dict[str, bool] | None = ...,
    ) -> HttpResponse: ...
    def changelist_view(
        self, request: HttpRequest, extra_context: dict[str, str] | None = ...
    ) -> TemplateResponse: ...
    def get_deleted_objects(
        self, objs: QuerySet[Any], request: HttpRequest
    ) -> tuple[list[Any], dict[Any, Any], set[Any], list[Any]]: ...
    def delete_view(
        self,
        request: HttpRequest,
        object_id: str,
        extra_context: dict[str, str] | None = ...,
    ) -> HttpResponse: ...
    def history_view(
        self,
        request: HttpRequest,
        object_id: str,
        extra_context: dict[str, str] | None = ...,
    ) -> HttpResponse: ...
    def get_formset_kwargs(
        self,
        request: HttpRequest,
        obj: _ModelT,
        inline: InlineModelAdmin[Any],
        prefix: str,
    ) -> dict[str, Any]: ...

class InlineModelAdmin(BaseModelAdmin[_ModelT]):
    model: type[_ModelT] = ...
    fk_name: str = ...
    formset: type[BaseInlineFormSet] = ...
    extra: int = ...
    min_num: int | None = ...
    max_num: int | None = ...
    template: str = ...
    verbose_name: str | None = ...
    verbose_name_plural: str | None = ...
    can_delete: bool = ...
    show_change_link: bool = ...
    classes: Sequence[str] | None = ...
    admin_site: AdminSite = ...
    parent_model: Any = ...
    opts: Any = ...
    has_registered_model: Any = ...
    def __init__(
        self, parent_model: type[_ModelT] | _ModelT, admin_site: AdminSite
    ) -> None: ...
    @property
    def media(self) -> Media: ...
    def get_extra(
        self, request: HttpRequest, obj: _ModelT | None = ..., **kwargs: Any
    ) -> int: ...
    def get_min_num(
        self, request: HttpRequest, obj: _ModelT | None = ..., **kwargs: Any
    ) -> int | None: ...
    def get_max_num(
        self, request: HttpRequest, obj: _ModelT | None = ..., **kwargs: Any
    ) -> int | None: ...
    def get_formset(
        self, request: HttpRequest, obj: _ModelT | None = ..., **kwargs: Any
    ) -> type[BaseInlineFormSet]: ...

class StackedInline(InlineModelAdmin[_ModelT]): ...
class TabularInline(InlineModelAdmin[_ModelT]): ...
